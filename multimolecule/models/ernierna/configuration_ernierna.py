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

from typing import Optional

from ..configuration_utils import BaseHeadConfig, HeadConfig, MaskedLMHeadConfig, PreTrainedConfig


class ErnieRnaConfig(PreTrainedConfig):
    r"""
    This is the configuration class to store the configuration of a
    [`ErnieRnaModel`][multimolecule.models.ErnieRnaModel]. It is used to instantiate a ErnieRna model according to the
    specified arguments, defining the model architecture. Instantiating a configuration with the defaults will yield a
    similar configuration to that of the ErnieRna [Bruce-ywj/ERNIE-RNA](https://github.com/Bruce-ywj/ERNIE-RNA)
    architecture.

    Configuration objects inherit from [`PreTrainedConfig`][multimolecule.models.PreTrainedConfig] and can be used to
    control the model outputs. Read the documentation from [`PreTrainedConfig`][multimolecule.models.PreTrainedConfig]
    for more information.

    Args:
        vocab_size:
            Vocabulary size of the ErnieRna model. Defines the number of different tokens that can be represented by
            the `inputs_ids` passed when calling [`ErnieRnaModel`].
        hidden_size:
            Dimensionality of the encoder layers and the pooler layer.
        num_hidden_layers:
            Number of hidden layers in the Transformer encoder.
        num_attention_heads:
            Number of attention heads for each attention layer in the Transformer encoder.
        intermediate_size:
            Dimensionality of the "intermediate" (often named feed-forward) layer in the Transformer encoder.
        hidden_act:
            The non-linear activation function (function or string) in the encoder and pooler. If string, `"gelu"`,
            `"relu"`, `"silu"` and `"gelu_new"` are supported.
        hidden_dropout:
            The dropout probability for all fully connected layers in the embeddings, encoder, and pooler.
        attention_dropout:
            The dropout ratio for the attention probabilities.
        max_position_embeddings:
            The maximum sequence length that this model might ever be used with. Typically set this to something large
            just in case (e.g., 512 or 1024 or 2048).
        initializer_range:
            The standard deviation of the truncated_normal_initializer for initializing all weight matrices.
        layer_norm_eps:
            The epsilon used by the layer normalization layers.
        position_embedding_type:
            Type of position embedding. Choose one of `"absolute"`, `"relative_key"`, `"relative_key_query"`,
            `"sinusoidal"`.
            For positional embeddings use `"absolute"`. For more information on `"relative_key"`, please refer to
            [Self-Attention with Relative Position Representations (Shaw et al.)](https://arxiv.org/abs/1803.02155).
            For more information on `"relative_key_query"`, please refer to *Method 4* in [Improve Transformer Models
            with Better Relative Position Embeddings (Huang et al.)](https://arxiv.org/abs/2009.13658).
        is_decoder:
            Whether the model is used as a decoder or not. If `False`, the model is used as an encoder.
        use_cache:
            Whether or not the model should return the last key/values attentions (not used by all models). Only
            relevant if `config.is_decoder=True`.
        head:
            The configuration of the head.
        lm_head:
            The configuration of the masked language model head.

    Examples:
        >>> from multimolecule import ErnieRnaConfig, ErnieRnaModel
        >>> # Initializing a ERNIE-RNA multimolecule/ernierna style configuration
        >>> configuration = ErnieRnaConfig()
        >>> # Initializing a model (with random weights) from the multimolecule/ernierna style configuration
        >>> model = ErnieRnaModel(configuration)
        >>> # Accessing the model configuration
        >>> configuration = model.config
    """

    model_type = "ernierna"

    def __init__(
        self,
        vocab_size: int = 26,
        hidden_size: int = 768,
        num_hidden_layers: int = 12,
        num_attention_heads: int = 12,
        intermediate_size: int = 3072,
        hidden_act: str = "gelu",
        hidden_dropout: float = 0.1,
        attention_dropout: float = 0.1,
        max_position_embeddings: int = 1026,
        initializer_range: float = 0.02,
        layer_norm_eps: float = 1e-12,
        position_embedding_type: str = "sinusoidal",
        pairwise_alpha: float = 0.8,
        is_decoder: bool = False,
        use_cache: bool = True,
        head: HeadConfig | None = None,
        lm_head: MaskedLMHeadConfig | None = None,
        output_attention_biases: bool = False,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.vocab_size = vocab_size
        self.type_vocab_size = 2
        self.hidden_size = hidden_size
        self.num_hidden_layers = num_hidden_layers
        self.num_attention_heads = num_attention_heads
        self.intermediate_size = intermediate_size
        self.hidden_act = hidden_act
        self.hidden_dropout = hidden_dropout
        self.attention_dropout = attention_dropout
        self.max_position_embeddings = max_position_embeddings
        self.initializer_range = initializer_range
        self.layer_norm_eps = layer_norm_eps
        self.position_embedding_type = position_embedding_type
        self.pairwise_alpha = pairwise_alpha
        self.is_decoder = is_decoder
        self.use_cache = use_cache
        self.head = HeadConfig(**head) if head is not None else None
        self.lm_head = MaskedLMHeadConfig(**lm_head) if lm_head is not None else None
        self.output_attention_biases = output_attention_biases


class ErnieRnaSecondaryStructureHeadConfig(BaseHeadConfig):
    r"""
    Configuration class for a prediction head.

    Args:
        num_labels:
            Number of labels to use in the last layer added to the model, typically for a classification task.

            Head should look for [`Config.num_labels`][multimolecule.PreTrainedConfig] if is `None`.
        problem_type:
            Problem type for `XxxForYyyPrediction` models. Can be one of `"binary"`, `"regression"`,
            `"multiclass"` or `"multilabel"`.

            Head should look for [`Config.problem_type`][multimolecule.PreTrainedConfig] if is `None`.
        dropout:
            The dropout ratio for the hidden states.
    """

    num_labels: int = 1
    problem_type: Optional[str] = None
    dropout: float = 0.3
    kernel_size: int = 7
    num_layers: int = 8
    num_channels: int = 64
    bias: bool = False
    activation: str = "relu"
