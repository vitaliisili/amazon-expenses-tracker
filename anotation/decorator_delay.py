import time


def progress_delay(prefix_msg: str = "Loading", suffix_msg="Complete", sec: int = 2):
    """ Show progres bar

    Usage: @progres_bar decorator decorate function that you want to show progres bar
    change <prefix_msg> to show custom message and <sec> for delay

    :param suffix_msg: (str) get custom suffix message default 'Complete'
    :param prefix_msg: (str) get custom prefix message default 'Loading'
    :param sec: (int) time in seconds for delay default 2 sec
    :return: (Callable) return inner function <func_wrapper>
    """

    def progress_bar(iteration, total=30, prefix=prefix_msg, suffix=suffix_msg, fill='█'):
        """ Print out a progress bar that updates with each iteration

        This would print out a progress bar that updates with each iteration of the loop.
        The prefix and suffix arguments are optional and can be used to customize the text
        displayed before and after the progress bar, respectively. The length argument determines
        the width of the progress bar, and the fill argument determines the character used to fill in the bar

        :param iteration: (int) The current iteration (progress).
        :param total: (int) The total iterations (total progress)
        :param prefix: (str) A prefix string to be printed before the progress bar.
        :param suffix: (str) A suffix string to be printed after the progress bar
        :param fill: The character used to fill the progress bar.
        :return: (None) Print progress bar with each iteration
        """
        percent = ("{0:." + "1" + "f}").format(100 * (iteration / float(total)))
        filled_length = int(30 * iteration // total)
        bar = fill * filled_length + '-' * (30 - filled_length)
        print(f'\r{prefix} |{bar}| {percent}% {suffix}', end="")

    def func_wrapper(func):
        def delay(*args, **kwargs):
            """ delay call for main function

            Delay main function call to specific seconds and show progres bar in command prompt

            :param args: (any) positional arguments
            :param kwargs: (any) named arguments
            :return: (Callable) return main function result
            """
            print()
            for i in range(30):
                progress_bar(i + 1)
                time.sleep(sec / 30)
            else:
                print()

            return func(*args, **kwargs)

        return delay

    return func_wrapper
