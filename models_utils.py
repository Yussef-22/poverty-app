# models_utils.py
# comment: Build the DF exactly as best_model (pipeline) expects

import pandas as pd

# comment: These are the columns the pipeline expects
ORIGINAL_COLUMNS = [
    'country', 'is_urban', 'age', 'female', 'married', 'religion',
    'relationship_to_hh_head', 'education_level', 'literacy', 'can_add',
    'can_divide', 'can_calc_percents', 'can_calc_compounding',
    'employed_last_year', 'employment_category_last_year',
    'employment_type_last_year', 'share_hh_income_provided',
    'income_ag_livestock_last_year', 'income_friends_family_last_year',
    'income_government_last_year', 'income_own_business_last_year',
    'income_private_sector_last_year', 'income_public_sector_last_year',
    'num_times_borrowed_last_year', 'borrowing_recency',
    'formal_savings', 'informal_savings', 'cash_property_savings',
    'has_insurance', 'has_investment', 'bank_interest_rate',
    'mm_interest_rate', 'mfi_interest_rate', 'other_fsp_interest_rate',
    'num_shocks_last_year', 'avg_shock_strength_last_year',
    'borrowed_for_emergency_last_year',
    'borrowed_for_daily_expenses_last_year',
    'borrowed_for_home_or_biz_last_year', 'phone_technology',
    'can_call', 'can_text', 'can_use_internet', 'can_make_transaction',
    'phone_ownership', 'advanced_phone_use', 'reg_bank_acct',
    'reg_mm_acct', 'reg_formal_nbfi_account', 'financially_included',
    'active_bank_user', 'active_mm_user', 'active_formal_nbfi_user',
    'active_informal_nbfi_user', 'nonreg_active_mm_user',
    'num_formal_institutions_last_year',
    'num_informal_institutions_last_year',
    'num_financial_activities_last_year'
]

# comment: Categories for country — NOT categorical dtype, just strings
VALID_COUNTRIES = ["C", "A", "D", "G", "F", "I", "J"]

# comment: Columns that were originally strings (needed for OneHotEncoder)
CAT_COLS = [
    "country", "religion", "relationship_to_hh_head",
    "employment_category_last_year", "employment_type_last_year"
]

def build_full_feature_df(user_inputs: dict):
    df = pd.DataFrame([{col: None for col in ORIGINAL_COLUMNS}])

    # Required fields (from user)
    df.loc[0, "country"] = user_inputs["country"]
    df.loc[0, "age"] = user_inputs["age"]
    df.loc[0, "is_urban"] = user_inputs["is_urban"]
    df.loc[0, "female"] = user_inputs["female"]
    df.loc[0, "education_level"] = user_inputs["education_level"]
    df.loc[0, "num_shocks_last_year"] = user_inputs["num_shocks_last_year"]
    df.loc[0, "avg_shock_strength_last_year"] = user_inputs["num_shocks_last_year"]

    # Set defaults for categoricals (strings, not numbers)
    for col in CAT_COLS:
        if df.loc[0, col] is None:
            df.loc[0, col] = "Unknown"

    # Fill missing numerical columns with 0
    for col in df.columns:
        if df[col].dtype != object and pd.isna(df.loc[0, col]):
            df.loc[0, col] = 0

    return df
