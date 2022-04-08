#' Filters a column in a data set for rows that contain a specified value
#'
#' Removes all rows that do not contain specified value in given column
#' from the data set
#' 
#' @param data A data frame or data frame extension (e.g. a tibble)
#' @param col quote colun name of column containing data that should be removed
#' @param val a value to be filtered for
#'
#' @return A data frame with only rows that contain the specified value in the 
#' given column
#'
#' @export
#'
#' @examples
#' filter(df, education, " Bachelors")
from pandas import DataFrame as DF

def filter(data, col, value):
    
    if type(data) != DF:
        raise Exception("Expected DataFrame, got", type(data))
    
    return data[data[col].str.contains(value)]