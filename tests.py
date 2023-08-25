import unittest
import abalyzer


class ExperimentConfidenceTests(unittest.TestCase):
    def test_sample_size_function_returns_correct_values(self):
        self.assertEqual(abalyzer.sample_size(0.13, 0.15), 4720)
        self.assertEqual(abalyzer.sample_size(0.7, 0.75), 1250)
        self.assertEqual(abalyzer.sample_size(0.11, 0.1155, alpha=0.01, power=0.95),
                         117808)

    def test_ztest_function_returns_correct_values(self):
        original = 285000
        conversions_original = 5940
        variation = 284870
        conversions_variation = 6178
        self.assertEqual(abalyzer.interpret(original_count=original, original_conversions=conversions_original,
                                            variation_count=variation, variation_conversions=conversions_variation, ),
                         {
                             'p_value': 0.0271,
                             'z_score': 2.2108,
                             'ci_original': [0.0203, 0.0214],
                             'ci_variation': [0.0212, 0.0222],
                             'uplift': 0.0405,
                             'prop_original': 0.0208,
                             'prop_variation': 0.0217,
                         })

    def test_lambda_handler_may_return_required_sample_size(self):
        self.assertEqual(abalyzer.lambda_handler({"func": "size", "args": [0.13, 0.15]}), {"size": 4720})
        self.assertEqual(abalyzer.lambda_handler({"func": "size", "args": [0.11, 0.1155],
                                                  "kwargs": {"alpha": 0.01, "power": 0.95}
                                                  }), {"size": 117808})

    def test_lambda_handler_returns_interpret_output(self):
        self.assertEqual(abalyzer.lambda_handler(
            {"kwargs": {
                "original_count": 34256,
                "original_conversions": 6245,
                "variation_count": 33568,
                "variation_conversions": 6178
                }
             }),
            {
                'p_value': 0.5579,
                'z_score': 0.5859,
                'ci_original': [0.1782, 0.1864],
                'ci_variation': [0.1799, 0.1882],
                'uplift': 0.0095,
                'prop_original': 0.1823,
                'prop_variation': 0.184,
            }
        )
