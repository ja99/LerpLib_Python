class Lerp:
    @staticmethod
    def lerp(a: float, b: float, t: float, clamped: bool = False) -> float:
        """
        Interpolates between to values by an amount t
        :param a: low value
        :param b: high value
        :param t: how much to interpolate (or extrapolate) between a and b
        :param clamped: whether to clamp the output between a and b or not
        :return: the interpolated value between a and b
        """
        if clamped:
            t = max(t, 0)
            t = min(t, 1)
        return a + ((b - a) * t)

    @staticmethod
    def inverse_lerp(a: float, b: float, val: float, clamped: bool = False) -> float:
        """
        Determines how far along the way beteewn a and b a value val is
        :param a: low value
        :param b: high value
        :param val: value between (or outside) of a and b
        :param clamped: whether to clamp the output t between 0 and 1 or not
        :return: the interpolated value between a and b
        """
        t = ((val - a) / (b - a))
        if clamped:
            t = max(t, 0)
            t = min(t, 1)
        return t

    @staticmethod
    def rescale(original_scale: tuple, original_val: float, output_scale: tuple, clamped: bool = False) -> float:
        """
        Rescales a value val from its original scale to a new scale
        :param original_scale: tuple(low, high) of original scale
        :param original_val: original value that should be rescaled
        :param output_scale: tuple(low, high) of output scale, that original_val should be scaled to
        :param clamped: whether to clamp the output value between the output scale or not
        :return: the rescaled value
        """

        t = Lerp.inverse_lerp(*original_scale, original_val, clamped)
        return Lerp.lerp(*output_scale, t)

