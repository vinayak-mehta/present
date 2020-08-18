# -*- coding: utf-8 -*-

import re
import time
from random import randint, choice

from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.effects import Print
from asciimatics.event import KeyboardEvent
from asciimatics.exceptions import ResizeScreenError, StopApplication, NextScene
from asciimatics.renderers import Box, StaticRenderer, FigletText, ColourImageFile

from .effects import explosions


class Text(StaticRenderer):
    def __init__(self, text):
        super(Text, self).__init__()
        self._images = [text]


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
        self.reset = self.reset_effect()
        self.line_height = self.screen.height / 20.0
        self.slides = [
            Slide(self, self.to_effects(slide), slide.fg_color, slide.bg_color)
            for slide in slides
        ]

        super(Slideshow, self).__init__()

    def reset_effect(self):
        reset = [
            Print(
                self.screen, Text("Press r to restart!"), int(self.screen.height / 2),
            ),
        ]

        return [Slide(self, reset, 7, 0)]

    def to_effects(self, slide):
        effects = []
        style = None
        fg_color, bg_color = 0, 7
        elements = slide.elements

        if slide.has_style:
            style = elements[0].style
            fg_color, bg_color = 7, 0
            elements = elements[1:]

        for e in elements:
            if e.type == "heading":
                if e.obj["level"] == 1:
                    height_factor = 6
                else:
                    height_factor = 4
            else:
                height_factor = 2

            if e.type == "image":
                effects.append(
                    Print(
                        self.screen,
                        ColourImageFile(
                            self.screen,
                            e.obj["src"],
                            int(self.screen.height / 2),
                            bg=bg_color,
                            fill_background=True,
                            uni=self.screen.unicode_aware,
                            dither=self.screen.unicode_aware,
                        ),
                        int(
                            self.screen.height / 2 - (height_factor * self.line_height)
                        ),
                    )
                )
            else:
                effects.append(
                    Print(
                        self.screen,
                        Text(e.render()),
                        int(
                            self.screen.height / 2 - (height_factor * self.line_height)
                        ),
                        colour=fg_color,
                        bg=bg_color,
                    )
                )
                height_factor -= 1

        if style is not None:
            _style = eval(style)(self.screen)
            effects.extend(list(_style))

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
