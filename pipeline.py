from feature_stage.utils.utils import split_user_full_name


def create_or_get_user(fullname: str):

    #[STEP 1] Given fullname (ex. giulio federico) as a string, split it into name and surname
    first_name, last_name = split_user_full_name(fullname)



