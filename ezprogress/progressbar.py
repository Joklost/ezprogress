import sys
import datetime


class StartException(Exception):
    def __init__(self):
        super().__init__('Please call ProgressBar.start() only once before ProgressBar.update()!')


class ProgressBar(object):

    def __init__(self, total: int, title: str = "", precision: int = 1, bar_length: int = 100, auto_start: bool = False):
        """
        Simple progress bar.

        >>> from ezprogress.progressbar import ProgressBar
        >>> pb = ProgressBar(total=100, title='Progress')
        >>> pb.start()
        >>> for i in range(0, 100):
        >>>     pb.update(i)
        >>>     do_stuff(i)
        >>> pb.finished()

        :param total: Total amount of iterations.
        :param title: To be printed on a line before the progressbar.
        :param precision: Number of % decimals to print.
        :param bar_length: Length of ProgressBar.
        :param auto_start: Immediately start the ProgressBar.
        """
        self._bar_length = bar_length
        self._decimals = precision
        self._title = title
        self._total = total
        self._start_time = None
        if auto_start:
            self.start()

    def start(self):
        if self._start_time:
            raise StartException()

        if self._title:
            sys.stdout.write(f'\n{self._title}:\n')

        self._start_time = datetime.datetime.utcnow()
        self._print(0, self._start_time)

    def finished(self):
        self.update(self._total)

    def update(self, iteration: int):
        if not self._start_time:
            raise StartException()

        self._print(iteration, datetime.datetime.utcnow())

    def _print(self, iteration: int, time: datetime.datetime):
        delta = time - self._start_time
        percent_value = 100 * (iteration / float(self._total))

        if percent_value:
            time_remaining = ((100 - percent_value) / percent_value) * delta
        else:
            time_remaining = datetime.timedelta(seconds=1)

        filled_length = int(round(self._bar_length * iteration / float(self._total)))
        bar = '█' * filled_length + '-' * (self._bar_length - filled_length)

        time_string = f'EST: {str(time_remaining).split(".")[0]}'
        sys.stdout.write(
            f'\r[{bar}] {percent_value:.{self._decimals}f} % {time_string if iteration != self._total else ""}'
        )
        if iteration == self._total:
            sys.stdout.write('\n')
        sys.stdout.flush()

