##############################################################################
# Copyright (c) 2013-2017, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/spack/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *


class PyPyvcf(PythonPackage):
    """PyVCF - A Variant Call Format Parser for Python"""

    homepage = "https://github.com/jamescasbon/PyVCF"
    url      = "https://pypi.io/packages/source/P/PyVCF/PyVCF-0.6.8.tar.gz"

    version('0.6.8', '3cc70aa59e62dab7b4a85bd5a9f2e714')
    version('0.6.7', '51b57ce99e0c2f7be2a18d08d8f87734')

    depends_on('py-setuptools', type='build')
    depends_on('py-cython', type='build')
    depends_on('py-pysam', type=('build', 'run'))
