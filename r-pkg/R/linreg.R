
#' @title Fit an mx + b linear regression
#' @name linreg
#' @description Given a 1-column matrix with a numeric target ("Y")
#'              and a 1-column matrix with numeric values of some
#'              explanatory variable ("X"), this function fits a simple
#'              linear regression with an intercept
#' @export
linreg <- function(X, Y){

    # if (is.vector(X)){
    #     X <- as.matrix(X)
    # }

    # if (is.vector(Y)){
    #     Y <- as.matrix(Y)
    # }

    intercept <- as.double(0)
    slope <- as.double(0)
    res <- .C(
        'linreg'
        , n = length(X)
        , X = X
        , Y = Y
        , m = slope
        , b = intercept
        , PACKAGE = "libadd_one"
    )

    eq_msg <- sprintf(
        "Y = %1.3f*X + %1.3f"
        , res[["m"]]
        , res[["b"]]
    )
    print("Done training. Model: ")
    print(eq_msg)

    return(res[c('m', 'b')])
}
