from math import ceil

import statsmodels.api as sm


def sample_size(current_conversion, desired_conversion, alpha=0.05, power=0.8):
    effect_size = sm.stats.proportion_effectsize(current_conversion, desired_conversion)
    return ceil(sm.stats.zt_ind_solve_power(effect_size=effect_size, nobs1=None, alpha=alpha, power=power))


def interpret(original_count, original_conversions, variation_count, variation_conversions, alpha=0.05):
    conversions = [variation_conversions, original_conversions]
    observations = [variation_count, original_count]
    prop_variation = variation_conversions / variation_count
    prop_original = original_conversions / original_count
    z_score, p = sm.stats.proportions_ztest(conversions, observations)
    (ci_v_low, ci_o_low), (ci_v_high, ci_o_high) = sm.stats.proportion_confint(conversions, observations, alpha=alpha)
    return {
        'z_score': round(z_score, 4),
        'p_value': round(p, 4),
        'ci_variation': [round(ci_v_low, 4), round(ci_v_high, 4)],
        'ci_original': [round(ci_o_low, 4), round(ci_o_high, 4)],
        'prop_variation': round(prop_variation, 4),
        'prop_original': round(prop_original, 4),
        'uplift': round((prop_variation - prop_original) / prop_original, 4),
    }


def lambda_handler(event, *args, **kwargs):
    if event.get('func') == 'size':
        return {'size': sample_size(*event['args'], **event.get('kwargs', {}))}
    return interpret(**event['kwargs'])
