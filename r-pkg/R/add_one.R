
#' @title add one
#' @name add_one
#' @description your mom
#' @href {stuff}{https://stackoverflow.com/a/42705521}
#' @export
add_one <- function(n){
    out <- .C('add_one', as.integer(n), PACKAGE = "libadd_one")
    return(out[[1]])
}
