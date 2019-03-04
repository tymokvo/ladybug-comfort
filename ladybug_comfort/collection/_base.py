# coding=utf-8
"""Comfort data collection base object."""

from ladybug._datacollectionbase import BaseCollection


class ComfortDataCollection(object):
    """Thermal comfort datacollection base class."""
    _model = None

    def __init__(self):
        self._calc_length = 0
        self._base_collection = None

    @property
    def comfort_model(self):
        """Return the name of the model to which the comfort datacollection belongs."""
        return self._model

    @property
    def calc_length(self):
        """The number of values in the Data Collections of this object."""
        return self._calc_length

    def _check_datacoll(self, data_coll, dat_type, unit, name):
        """Check the data type and units of a Data Collection."""
        if isinstance(data_coll, BaseCollection):
            assert isinstance(data_coll.header.data_type, dat_type) and \
                data_coll.header.unit == unit, '{} must be {} in {}. ' \
                'Got {} in {}'.format(name, dat_type.name, unit,
                                      data_coll.header.data_type.name,
                                      data_coll.header.unit)
            self._input_collections.append(data_coll)
            return data_coll
        else:
            try:
                return self._base_collection.get_aligned_collection(
                    float(data_coll), dat_type(), unit)
            except ValueError:
                raise TypeError('{} must be either a number or a Data Colleciton. '
                                'Got {}'.format(name, type(data_coll)))

    def _build_coll(self, value_list, dat_type, unit):
        return self._base_collection.get_aligned_collection(value_list, dat_type, unit)

    def ToString(self):
        """Overwrite .NET ToString."""
        return self.__repr__()

    def __repr__(self):
        """Comfort model representation."""
        return "{} Comfort Model\n{} values".format(
            self.comfort_model, self._calc_length)
