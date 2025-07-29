#!/usr/bin/env python3
"""
Main module for the application.
"""
# ruff: noqa: F405

from manim import *  # type: ignore  # noqa: F403
from manim.utils.color.XKCD import ORANGEPINK


class YoutubeLogo(Scene):
    def construct(self):
        self.camera.background_color = ORANGEPINK  # type: ignore

        squigglyLine1 = (
            SVGMobject("assets/blog-line-pt.svg")
            .move_to(config.frame_width / 3 * LEFT + config.frame_height / 3 * DOWN)
            .set_color(BLACK)
        )
        squigglyLine2 = (
            SVGMobject("assets/blog-line-pt.svg")
            .flip(UP)
            .flip(RIGHT)
            .move_to(config.frame_width / 3 * RIGHT + config.frame_height / 3 * UP)
            .set_color(BLACK)
        )
        self.add(squigglyLine1, squigglyLine2)
        self.play(
            DrawBorderThenFill(squigglyLine1),
            DrawBorderThenFill(squigglyLine2),
            run_time=2,
        )

        youtubeName = Text("Ragg", color=BLACK, font_size=72)
        self.add(youtubeName)
        self.play(DrawBorderThenFill(youtubeName), run_time=2)
        self.play(youtubeName.animate.rotate(-10 * DEGREES), run_time=0.5)

        self.play(FadeOut(squigglyLine1, squigglyLine2, youtubeName))

        self.wait(1)
