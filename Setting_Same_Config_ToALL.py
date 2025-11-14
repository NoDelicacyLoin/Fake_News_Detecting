    ''' The universal config for every model, these are the main config
        the others we use defualt
    '''
Config_Universal = dict(
    max_input_length=256,
    max_new_tokens=64,   # if == 4, only generate "True"/"False"
    random_seed=42,
    train_epochs=3,
    batch_size_train=8,
    batch_size_eval=16,
    gradient_accumulation_steps=4,
    sampling_on = False
)

def get_generation_kwargs_from_setting(config_dict, do_sample):
    if do_sample == True:
      return dict( do_sample = True,
        temperature = 1.0, top_k = 50, top_p = 0.9,
        max_new_tokens = config_dict["max_new_tokens"],
        return_full_text = False, truncation = True,
        max_length = config_dict["max_input_length"],
        num_beams=1 )

    return dict( do_sample =False,
        max_new_tokens = config_dict["max_new_tokens"],
        return_full_text = False, truncation=True,
        max_length = config_dict["max_input_length"] 
        num_beams=1 )
