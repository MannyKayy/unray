import numpy as np
import ipywidgets as widgets
from ipywidgets import widget_serialization, register
from ipydatawidgets import DataUnion, data_union_serialization, shape_constraints
from traitlets import Unicode, List, Dict, Any, CFloat, CInt, CBool, Enum
from traitlets import Instance, TraitError, TraitType, Undefined
from ._version import widget_module_name, widget_module_version

# List of valid field types
field_types = ("P0", "P1", "D1")

# List of valid indicator field types
indicator_field_types = ("I0", "I1", "I2", "I3")


class BaseWidget(widgets.Widget):
    # Abstract class, don't register, and don't set name
    _model_module = Unicode(widget_module_name).tag(sync=True)
    _model_module_version = Unicode(widget_module_version).tag(sync=True)


# ------------------------------------------------------


@register
class Mesh(BaseWidget):
    """Representation of an unstructured mesh."""
    _model_name = Unicode('MeshModel').tag(sync=True)
    auto_orient = CBool(True).tag(sync=True)
    cells = DataUnion(dtype=np.int32, shape_constraint=shape_constraints(None, 4)).tag(sync=True)    
    points = DataUnion(dtype=np.float32, shape_constraint=shape_constraints(None, 3)).tag(sync=True)


@register
class Field(BaseWidget):
    """Representation of a discrete scalar field over a mesh."""
    _model_name = Unicode('FieldModel').tag(sync=True)
    mesh = Instance(Mesh, allow_none=False).tag(sync=True, **widget_serialization)
    values = DataUnion(dtype=np.float32, shape_constraint=shape_constraints(None)).tag(sync=True, **data_union_serialization)
    space = Enum(field_types, "P1").tag(sync=True)


@register
class IndicatorField(BaseWidget):
    """Representation of a set of nominal indicator values for each mesh entity."""
    _model_name = Unicode('IndicatorFieldModel').tag(sync=True)
    mesh = Instance(Mesh, allow_none=False).tag(sync=True, **widget_serialization)
    values = DataUnion(dtype=np.int32, shape_constraint=shape_constraints(None)).tag(sync=True, **data_union_serialization)
    space = Enum(indicator_field_types, "I3").tag(sync=True)


# ------------------------------------------------------


@register
class WireframeParams(BaseWidget):
    """Collection of wireframe parameters."""
    _model_name = Unicode('WireframeParamsModel').tag(sync=True)
    enable = CBool(True).tag(sync=True)
    size = CFloat(0.001).tag(sync=True)
    color = Unicode("#000000").tag(sync=True)
    opacity = CFloat(1.0).tag(sync=True)


# ------------------------------------------------------
# TODO: Lookup tables for scalars and colors should be
# developed further in ipyscales or shared with some other project

class LUT(BaseWidget):
    """Representation of a lookup table."""
    # Abstract class, don't register, and don't set name


class ScalarLUT(LUT):
    """Representation of a scalar lookup table."""
    # Abstract class, don't register, and don't set name


@register
class ArrayScalarLUT(ScalarLUT):
    """Representation of a scalar lookup table by an array of values."""
    _model_name = Unicode('ArrayScalarLUTModel').tag(sync=True)
    values = DataUnion(dtype=np.float32, shape_constraint=shape_constraints(None)).tag(sync=True, **data_union_serialization)
    #space = Enum(["linear", "log", "power"], "linear").tag(sync=True)


# @register
# class NamedScalarLUT(ScalarLUT):
#     """Representation of a scalar lookup table by name."""
#     _model_name = Unicode('NamedScalarLUTModel').tag(sync=True)
#     name = Unicode("linear").tag(sync=True)


class ColorLUT(LUT):
    """Representation of a color lookup table."""
    # Abstract class, don't register, and don't set name


@register
class ArrayColorLUT(ColorLUT):
    """Representation of a color lookup table by an array of values."""
    _model_name = Unicode('ArrayColorLUTModel').tag(sync=True)
    values = DataUnion(dtype=np.float32, shape_constraint=shape_constraints(None, 3)).tag(sync=True, **data_union_serialization)
    space = Enum(["rgb", "hsv"], "rgb").tag(sync=True)


@register
class NamedColorLUT(ColorLUT):
    """Representation of a color lookup table by name."""
    _model_name = Unicode('NamedColorLUTModel').tag(sync=True)
    name = Unicode("viridis").tag(sync=True)


# ------------------------------------------------------


class Scalar(BaseWidget):
    """Representation of a scalar quantity."""
    # Abstract class, don't register, and don't set name
    pass


@register
class ScalarConstant(Scalar):
    """Representation of a scalar constant."""
    _model_name = Unicode('ScalarConstantModel').tag(sync=True)

    value = CFloat(0.0).tag(sync=True)


@register
class ScalarField(Scalar):
    """Representation of a scalar field."""
    _model_name = Unicode('ScalarFieldModel').tag(sync=True)

    field = Instance(Field, allow_none=False).tag(sync=True, **widget_serialization)
    lut = Instance(ScalarLUT, allow_none=True).tag(sync=True, **widget_serialization)


@register
class ScalarIndicators(Scalar):
    """Representation of a scalar constant for each mesh entity."""
    _model_name = Unicode('ScalarIndicatorsModel').tag(sync=True)

    # TODO: Validate field spaces: ["I2", "I3"]
    field = Instance(IndicatorField, allow_none=False).tag(sync=True, **widget_serialization)
    lut = Instance(ScalarLUT, allow_none=True).tag(sync=True, **widget_serialization)


# ------------------------------------------------------


class Color(BaseWidget):
    """Representation of a color quantity."""
    # Abstract class, don't register, and don't set name
    pass


@register
class ColorConstant(Color):  # TODO: Use something from ipywidgets or other generic library
    """Representation of a constant color."""
    _model_name = Unicode('ColorConstantModel').tag(sync=True)

    intensity = CFloat(1.0).tag(sync=True)
    color = Unicode("#ffffff").tag(sync=True)


@register
class ColorField(Color):
    """Representation of a color field."""
    _model_name = Unicode('ColorFieldModel').tag(sync=True)

    field = Instance(Field, allow_none=False).tag(sync=True, **widget_serialization)
    lut = Instance(ColorLUT, allow_none=True).tag(sync=True, **widget_serialization)


@register
class ColorIndicators(Color):
    """Representation of a color constant for each mesh entity."""
    _model_name = Unicode('ColorIndicatorsModel').tag(sync=True)

    # TODO: Validate field spaces: ["I2", "I3"]
    field = Instance(IndicatorField, allow_none=False).tag(sync=True, **widget_serialization)
    lut = Instance(ColorLUT, allow_none=True).tag(sync=True, **widget_serialization)


# ------------------------------------------------------