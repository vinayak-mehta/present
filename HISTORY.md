Release History
===============

master
------

* [#36](https://github.com/vinayak-mehta/present/issues/36) Add contributing guide. [#69](https://github.com/vinayak-mehta/present/pull/69) by Vinayak Mehta.

0.5.1 (2020-08-31)
------------------

**Bugfixes**

* [#48](https://github.com/vinayak-mehta/present/issues/48), [#54](https://github.com/vinayak-mehta/present/issues/54), [#52](https://github.com/vinayak-mehta/present/issues/52) Remove italics support temporarily. [#58](https://github.com/vinayak-mehta/present/pull/58) by Vinayak Mehta.
* [#55](https://github.com/vinayak-mehta/present/issues/55) Yank versions older than `0.5.0` from PyPI because they didn't have `python_requires>=3.7`.

0.5.0 (2020-08-30)
------------------

**Enhancements**

* [#26](https://github.com/vinayak-mehta/present/issues/26) Add codio support. [#20](https://github.com/vinayak-mehta/present/pull/20) by Vinayak Mehta.
* [#35](https://github.com/vinayak-mehta/present/issues/35) Support bold/italic text, inline code, links and block quotes. [#38](https://github.com/vinayak-mehta/present/pull/38) by Vinayak Mehta.
* [#32](https://github.com/vinayak-mehta/present/issues/32) Make level 3 headings bold. [#33](https://github.com/vinayak-mehta/present/pull/33) by Vinayak Mehta.
* Allow pressing spacebar to go to next slide. [#30](https://github.com/vinayak-mehta/present/pull/30) by [Thomas Royal](https://github.com/tmroyal).
* [#27](https://github.com/vinayak-mehta/present/issues/27) Don't raise an error for unsupported markdown elements. [#34](https://github.com/vinayak-mehta/present/pull/34) by Vinayak Mehta.
* Unvendor `mistune`.

**Bugfixes**

* [#28](https://github.com/vinayak-mehta/present/issues/28) Render single elements using mid point. [#31](https://github.com/vinayak-mehta/present/pull/31) by Vinayak Mehta.

0.4.0 (2020-08-27)
------------------

**Enhancements**

* Allow `Slideshow` to be used as a context manager. [#18](https://github.com/vinayak-mehta/present/pull/18) by [Clint Lawrence](https://github.com/clint-lawrence).

    Also, the earlier duct tape fix `os.system('reset')` (to not leave the terminal in an abnormal state after exit) is replaced with a `screen.close()` which is much better because the earlier fix wouldn't work on Windows.

* Move an element to the center when there is only one on a slide. [6a0b045](https://github.com/vinayak-mehta/present/commit/6a0b045d0837dc05729d45427c6fae66a1d197ad) by Vinayak Mehta.

0.3.0 (2020-08-20)
------------------

**Enhancements**

* [#17](https://github.com/vinayak-mehta/present/issues/17) Raise informative error when image file does not exist. [564fa72](https://github.com/vinayak-mehta/present/commit/564fa727ec66eda93684dfaa25b7f6f5a4033972) by Vinayak Mehta.

**Bugfixes**

* [#16](https://github.com/vinayak-mehta/present/issues/16) Add variable size for h1 headings. [446385d](https://github.com/vinayak-mehta/present/commit/446385d75690bac940e3eeb665b9118f10c8aed4) by Vinayak Mehta.

0.2.0 (2020-08-20)
------------------

* First working release!
