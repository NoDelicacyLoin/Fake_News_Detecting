
def prompt_setting(statement_text, setting_name):
    """
    - baseline: only statement given
    - instruction only: instruction + statement（Let model know its task）, make output True/False
    - CoT: instruction + CoT + statement. Short Rational first, then label output.
    """
    statement_text = str(statement_text)
    setting_name= str(setting_name).strip()

    # baseline: 只喂原句
    if setting_name == "baseline":
        return statement_text

    # instruction only: instruction + statement（Let model know its task）
    if setting_name == "instruction":
      return ("Instruction: Decide whether the following claim is true or false.\n"
          f'Statement: "{statement_text}"\n'
          "Options: True or False.\n"
          "Output the label only.")

    # instruction + CoT: instruction + CoT + statement（Let model know its task）
    if setting_name == "CoT":
        return ("Instruction: Decide whether the following claim is true or false.\n"
            "Before the final decision, briefly explain your reasoning in 1-2 sentences.\n"
            f'Statement: \"{statement_text}\"\n'
            "Options: True or False.\n"
            "Format:\n"
            "Reasoning: <short explanation>\n"
            "Final label: <True or False>.")

    raise ValueError("setting_name must be 'baseline', 'instruction', or 'CoT'.")


def build_TF_from_label(binary_label_int):
    # In label we used 1=true, 0=false but for model we use "True"/"False"
    return "True" if int(binary_label_int) == 1 else "False"



##### Prompt Test #############
test_case = test_df_b["statement"].iloc[2]
test_settings = ["baseline", "instruction", "CoT", "WHAT???"]
print( f"Statement: {test_case}\n")
print()
for setting_name in test_settings:
    print(f"--- prompt '{setting_name}' ---")
    try:
        prompt_text = prompt_setting(test_case, setting_name)
        print(prompt_text)
    except ValueError as err:
        # demonstration of illegal input (passing wrong prompt setting )
        print(f"[Error]: {err}")
    print()
print(test_df_b)

