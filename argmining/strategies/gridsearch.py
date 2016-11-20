import argmining.features.bag_of_words as bag_of_words
import argmining.features.pos_distribution as pos_distribution
import argmining.features.dependency_distribution as dependency_distribution
import argmining.features.structural_features as structural_features
from collections import OrderedDict

GRIDSEARCH_STRATEGIES = {
    'unigram':
        {
            'features':
                OrderedDict([
                    ('bag_of_words', bag_of_words.build)
                ]),
            'param_grid': {
                'union__bag_of_words__transformer__ngram': [1],
                'union__bag_of_words__transformer__lowercase': [True, False],
                'union__bag_of_words__transformer__token_form': ['text', 'IWNLP_lemma'],
                'union__bag_of_words__normalizer__use_normalize': [True, False],
            }
        },
    'bigram':
        {
            'features':
                OrderedDict([
                    ('bag_of_words', bag_of_words.build)
                ]),
            'param_grid': {
                'union__bag_of_words__transformer__ngram': [2],
                'union__bag_of_words__transformer__lowercase': [True, False],
                'union__bag_of_words__transformer__token_form': ['text', 'IWNLP_lemma'],
                'union__bag_of_words__normalizer__use_normalize': [True, False],
            }
        },
    'pos_distribution':
        {
            'features':
                OrderedDict([
                    ('pos_distribution', pos_distribution.build)
                ]),
            'param_grid': {
                'union__pos_distribution__transformer__use_STTS': [True, False],
            }
        },
    'pos_distribution_feature_selection':
        {
            'features':
                OrderedDict([
                    ('pos_distribution', pos_distribution.build_feature_selection)
                ]),
            'param_grid': [
                {
                    'union__pos_distribution__transformer__use_STTS': [True],
                    'union__pos_distribution__feature_selection__k': [5, 10, 15, 20, 30, 'all'],
                },
                {
                    'union__pos_distribution__transformer__use_STTS': [False],
                    'union__pos_distribution__feature_selection__k': [6, 7, 8, 9, 10, 11, 'all'],
                }

            ]

        }
}