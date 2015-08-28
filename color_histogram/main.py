
# -*- coding: utf-8 -*-
## @package color_histogram.main
#
#  Main functions.
#  @author      tody
#  @date        2015/08/28

from color_histogram.datasets.google_image import createDatasets

from color_histogram.results.hist_2d import histogram2DResults

if __name__ == '__main__':
    data_names = ["flower"]
    num_images = 3
    data_ids = range(num_images)

    createDatasets(data_names, num_images, update=False)
    histogram2DResults(data_names, data_ids)