#!/usr/bin/env python3
"""
Main module for the application.
"""

from manim import *
from manim.utils.color.XKCD import ORANGEPINK


class YoutubeLogo(Scene):
    def construct(self):
        # Dynamic background color transition
        self.camera.background_color = BLACK

        # make reuseable global variables
        colors = [ORANGEPINK, RED, PINK]

        # Create a gradient background effect
        gradient_bg = Rectangle(
            width=config.frame_width,
            height=config.frame_height,
            fill_color=colors,
            fill_opacity=1,
            stroke_width=0,
        )
        self.add(gradient_bg)
        self.play(FadeIn(gradient_bg), run_time=1)

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

        youtubeName = Text("Ragg", font="Lobster", color=BLACK, font_size=72)
        text_shadow = (
            youtubeName.copy()
            .set_color_by_gradient(*colors)
            .shift(0.1 * DOWN + 0.1 * RIGHT)
        )
        self.add(text_shadow)
        self.add(youtubeName)
        self.play(
            DrawBorderThenFill(text_shadow),
            DrawBorderThenFill(youtubeName),
            run_time=2,
        )
        self.play(
            text_shadow.animate.rotate(-10 * DEGREES),
            youtubeName.animate.rotate(-10 * DEGREES),
            run_time=0.5,
        )

        self.play(
            FadeOut(
                squigglyLine1,
                squigglyLine2,
                text_shadow,
                youtubeName,
            )
        )

        self.wait()
