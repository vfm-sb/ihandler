# Python InputHandler History

<br>

## 0.1.4.2 (2024/06/19)

- Bugfix: Choice Inputs >> `_get_2d_choice_index()`
    - Now Returns Correct Index If a Keyword Input Received.
    - Utilities Using `_get_2d_choice_index()` **Require** v0.1.4.2!
        - `choice2d()`
        - `binary_choice()`


## 0.1.4.1 (2024/06/19)

- Choice Inputs:
    - `binary_choice()`


## 0.1.4 (2024/06/14)

- Choice Inputs:
    - `choice2d()`


## 0.1.3 (2024/03/05)

- Currency Inputs:
    - `currency_code()`
    - `alphabetic_currency_code()`
    - `numeric_currency_code()`


## 0.1.2 (2024/03/04)

- Choice Inputs:
    - `choice()`
    - `alphanumeric_choice()`, `numeric_choice()`
    - `lowercase_choice()`, `uppercase_choice()`, `letter_choice()`


## 0.1.1 (2024/03/02)

- Complete Design Change: Functions instead of Classes
- String Inputs:
    - `strict_string`, `unrestricted_string`, `lowercase_string`, `uppercase_string`,
    - `multiple_strings`,
- Numeric Inputs:
    - `strict_numeric`, `loose_numeric`, `strict_integer`, `loose_integer`,


## 0.1.0 (2024/02/27)

- Initial Running Version
- Initial Versions of `InputHandler` Class & `ihandler` Function
