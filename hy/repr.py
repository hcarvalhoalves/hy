# Copyright (c) 2013 Nicolas Dandrimont <nicolas.dandrimont@crans.org>
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

from hy.models.complex import HyComplex
from hy.models.dict import HyDict
from hy.models.expression import HyExpression
from hy.models.float import HyFloat
from hy.models.integer import HyInteger
from hy.models.keyword import HyKeyword, keyword_magic
from hy.models.lambdalist import HyLambdaListKeyword
from hy.models.list import HyList
from hy.models.string import HyString
from hy.models.symbol import HySymbol

from hy._compat import builtins, str_type

from itertools import chain

__all__ = ["HyRepr", "repr"]

hy_map = {
    str_type: lambda x: x.startswith(keyword_magic) and HyKeyword(x.strip(keyword_magic)) or HyString(x),
    dict: lambda x: HyDict(chain(*x.iteritems())),
    list: HyList,
    tuple: HyList,
}

builtin_repr = builtins.repr

def repr(x):
    try:
        hy_model = hy_map[type(x)]
    except KeyError:
        s = builtin_repr(x)
    else:
        s = hy_model(x).__repr__() # Wrap in HyModel
    return s

builtins.repr = repr
