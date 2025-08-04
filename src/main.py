#!/usr/bin/env python3
"""
Main module for the application.
"""

from manim import *  # noqa: F403
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

        # Animated entrance with bounce
        all_text = VGroup(text_shadow, youtubeName)
        all_text.scale(0.1)

        self.play(
            all_text.animate.scale(10),
            run_time=1.5,
            rate_func=rate_functions.ease_out_bounce
        )

        # Rotation with overshoot and settle
        self.play(
            all_text.animate.rotate(-15 * DEGREES),
            run_time=0.3,
        )
        self.play(
            all_text.animate.rotate(5 * DEGREES),
            run_time=0.2,
        )

        # Subtle floating animation
        self.play(
            all_text.animate.shift(0.1 * UP),
            run_time=1,
            rate_func=rate_functions.ease_in_out_sine
        )
        self.play(
            all_text.animate.shift(0.1 * DOWN),
            run_time=1,
            rate_func=rate_functions.ease_in_out_sine
        )

        # Enhanced exit with particle effect simulation
        particles = VGroup()
        for _ in range(20):
            particle = Dot(
                point=youtubeName.get_center() + np.random.uniform(-1, 1, 3),
                radius=0.05,
                color=np.random.choice(colors)
            )
            particles.add(particle)

        self.add(particles)

        # Simultaneous fade and particle dispersion
        self.play(
            FadeOut(squigglyLine1, squigglyLine2, all_text, gradient_bg),
            *[particle.animate.shift(
                np.random.uniform(-3, 3) * RIGHT +
                np.random.uniform(-3, 3) * UP
            ).fade(1) for particle in particles],
            run_time=2
        )

        self.wait()
