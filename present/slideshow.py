# -*- coding: utf-8 -*-

import time

from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.event import KeyboardEvent
from asciimatics.exceptions import ResizeScreenError, StopApplication

from .effects import _reset, _base, _image, _code, _explosions, _stars, _matrix, _plasma


class Slide(Scene):
    def __init__(self, show, effects, fg_color, bg_color):
        self.show = show
        self.fg_color = fg_color
        self.bg_color = bg_color
        super(Slide, self).__init__(effects)

    def process_event(self, event):
        if super(Slide, self).process_event(event) is None:
            return

        if isinstance(event, KeyboardEvent):
            c = event.key_code
            if c in (ord("b"), Screen.KEY_LEFT):
                self.show.current_slide -= 1

                try:
                    self.show.screen.set_scenes(
                        [self.show.slides[self.show.current_slide]]
                    )
                    self.show.screen.clear_buffer(
                        self.show.slides[self.show.current_slide].fg_color,
                        0,
                        self.show.slides[self.show.current_slide].bg_color,
                    )
                except IndexError:
                    pass
            elif c in (ord("n"), Screen.KEY_RIGHT):
                self.show.current_slide += 1

                try:
                    self.show.screen.set_scenes(
                        [self.show.slides[self.show.current_slide]]
                    )
                    self.show.screen.clear_buffer(
                        self.show.slides[self.show.current_slide].fg_color,
                        0,
                        self.show.slides[self.show.current_slide].bg_color,
                    )
                except IndexError:
                    pass
            else:
                return event
        else:
            return event


class Slideshow(object):
    def __init__(self, slides):
        self.reset = None
        self.current_slide = 0
        self.screen = Screen.open()
        self.reset = [Slide(self, _reset(self.screen), 7, 0)]
        self.lh = self.screen.height / 20.0
        self.slides = [
            Slide(self, self.get_effects(slide), slide.fg_color, slide.bg_color)
            for slide in slides
        ]

        super(Slideshow, self).__init__()

    def get_effects(self, slide):
        effects = []
        transparent = True
        elements = slide.elements
        fg_color, bg_color = slide.fg_color, slide.bg_color

        if slide.has_style:
            elements = elements[1:]

        row = 5
        pad = 2
        for e in elements:
            if e.type == "code":
                effects.extend(_code(self.screen, e, row))
                pad = 4
            elif e.type == "image":
                effects.extend(_image(self.screen, e, row, bg_color))
                pad = 2
            else:
                effects.extend(_base(self.screen, e, row, fg_color, bg_color))
                pad = 2

            row += e.size + pad

        if slide.has_style and slide.effect is not None:
            _effect = eval(f"_{slide.effect}")(self.screen)
            effects.extend(list(_effect))

        return effects

    def play(
        self,
        stop_on_resize=False,
        unhandled_input=None,
        start_scene=None,
        repeat=True,
        allow_int=False,
    ):
        # Initialise the Screen for animation.
        self.screen.set_scenes(
            self.slides, unhandled_input=unhandled_input, start_scene=start_scene
        )
        self.screen.clear_buffer(self.slides[0].fg_color, 0, self.slides[0].bg_color)

        # Mainline loop for animations
        try:
            while True:
                if self.current_slide == len(self.slides):
                    self.screen.set_scenes(self.reset)

                    while True:
                        a = time.time()
                        self.screen.draw_next_frame(repeat=repeat)
                        b = time.time()
                        if b - a < 0.05:
                            # Just in case time has jumped (e.g. time change), ensure we only delay for 0.05s
                            pause = min(0.05, a + 0.05 - b)
                            if allow_int:
                                self.screen.wait_for_input(pause)
                            else:
                                time.sleep(pause)

                        event = self.screen.get_event()
                        if isinstance(event, KeyboardEvent):
                            if event.key_code == ord("r"):
                                self.current_slide = 0
                                self.screen.set_scenes(
                                    [self.slides[self.current_slide]]
                                )
                                self.screen.clear_buffer(
                                    self.slides[self.current_slide].fg_color,
                                    0,
                                    self.slides[self.current_slide].bg_color,
                                )
                                break
                            else:
                                raise StopApplication("Stop slideshow")

                a = time.time()
                self.screen.draw_next_frame(repeat=repeat)
                if self.screen.has_resized():
                    if stop_on_resize:
                        self.screen._scenes[self.screen._scene_index].exit()
                        raise ResizeScreenError(
                            "Screen resized",
                            self.screen._scenes[self.screen._scene_index],
                        )
                b = time.time()
                if b - a < 0.05:
                    # Just in case time has jumped (e.g. time change), ensure we only delay for 0.05s
                    pause = min(0.05, a + 0.05 - b)
                    if allow_int:
                        self.screen.wait_for_input(pause)
                    else:
                        time.sleep(pause)
        except StopApplication:
            # Time to stop  - just exit the function.
            self.screen.clear()
            return
