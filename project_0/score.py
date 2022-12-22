import numpy as np
        
def random_predict(number:int=1) -> int:
    """Random number guessing function

    Args:
        number (int, optional): number to guess. Defaults to 1.

    Returns:
        int: number of tries
    """
    
    number_list = [] # number guess list
        
    def guess_number() -> int:
        """Number guessing optimization algorithm
        
        Args: none

        Returns:
            int: number to guess
        """
        
        global predict_number
        if number_list == []:
            predict_number = 50
        elif number > max(number_list):
            predict_number = np.random.randint(max(number_list),101)
        elif number < number_list[::-1][0] and number > np.mean(number_list):
            predict_number = np.random.randint(np.mean(number_list),number_list[::-1][0])
        elif number < number_list[::-1][0] and number < np.mean(number_list):
            predict_number = np.random.randint(1,np.mean(number_list))
        elif number > number_list[::-1][0] and number < max(number_list):
            predict_number = np.random.randint(number_list[::-1][0],max(number_list))
        elif number < number_list[::-1][0] and number < min(number_list):
            predict_number = np.random.randint(1,min(number_list))
        else:
            predict_number = np.random.randint(min(number_list), max(number_list))
        number_list.append(predict_number)
        return predict_number

    count = 0
    
    while True:
        """cycle to guess number""" 
        count += 1
        guess_number() # get output from optimization algorithm
        if number == predict_number:
            break # cycle exit in case of successful guess
    return(count)
    
def score_game(random_predict) -> int:
    """average guesses to guess number for array of 1000 numbers

    Args:
        random_predict ([type]): number guessing function

    Returns:
        int: average guesses
    """

    count_ls = [] # number of guesses list
    np.random.seed(1) # fix random seed 
    random_array = np.random.randint(1, 101, size=(1000)) # generate numbers to be guessed

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # average number of guesses 

    print(f'Average number of algorithm guesses: {score}')
    return(score)

# RUN
if __name__ == '__main__':
    score_game(random_predict)