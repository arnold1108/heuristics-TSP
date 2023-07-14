from tsp import my_towns, create_towns_dataframe, main 
import pytest

# A list of towns 
town_list = my_towns("Kericho", "Narok", "Makueni")

town_df = create_towns_dataframe(town_list)

@pytest.mark.slow
def test_my_towns():
    """Testing my_towns function"""
    assert my_towns("Kericho", "Narok", "Makueni")  == [
        "Kericho",
        "Narok",
        "Makueni"
    ]

@pytest.mark.slow
def test_main():
    """Testing my main function"""
    assert main(count=1) == None
    
