# MultiMolecule
# Copyright (C) 2024-Present  MultiMolecule

# This file is part of MultiMolecule.

# MultiMolecule is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.

# MultiMolecule is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# For additional terms and clarifications, please refer to our License FAQ at:
# <https://multimolecule.danling.org/about/license-faq>.


from __future__ import annotations

import os
from collections.abc import Mapping
from pathlib import Path

import torch
from tqdm import tqdm

from multimolecule.datasets.conversion_utils import ConvertConfig as ConvertConfig_
from multimolecule.datasets.conversion_utils import get_files, save_dataset

torch.manual_seed(1016)


def convert_dbn(file) -> Mapping:
    if not isinstance(file, Path):
        file = Path(file)
    with open(file) as f:
        lines = f.read().splitlines()
    if not len(lines) == 3:
        raise ValueError(f"Expected 3 lines, got {len(lines)}")
    id, sequence, secondary_structure = lines
    id = id[1:]
    if id != file.stem:
        raise ValueError(f"Expected id {file.stem}, got {id}")
    return {
        "id": id,
        "sequence": sequence,
        "secondary_structure": secondary_structure,
    }


def convert_dataset(convert_config):
    data = [convert_dbn(file) for file in tqdm(get_files(convert_config.dataset_path))]
    save_dataset(convert_config, data, filename="test.parquet")


class ConvertConfig(ConvertConfig_):
    root: str = os.path.dirname(__file__)
    output_path: str = os.path.basename(os.path.dirname(__file__)).replace("_", "-")


if __name__ == "__main__":
    config = ConvertConfig()
    config.parse()  # type: ignore[attr-defined]
    convert_dataset(config)
