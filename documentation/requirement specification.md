# Requirement specification

## The purpose of the software

The software allows users to track their finances, taking into account their various incomes and expenses.
Each user has their separate account that they can access with the login/registration window.

### Users

The application will only consist of normal users, as this software is meant to be used locally. Different user accounts
are still implemented e.g for use within families.

### User interface

The user interface consists of various windows, so the user can always see the main window if needed.
The login/registration window has shared fields for username and password. The main window consists of a treeview,
showing
the user's transactions, and a graph view with information on net values of entries on a given month.

## Functionality offered by the first iteration

The user can register and log in, add financial entries (income or expense), view previous entries in a list, as well as view the net value of entries for days in a given month.

## Further development ideas

- [x] Toggle between adding income or expense
- [x] Graph of (monthly?) income vs expenses
- [x] Entry deletion
- [ ] Planning budget ahead, (salary + income - expenses) for the upcoming month
- [ ] Category combobox, with the ability to add more categories
- [ ] Logging out
- [ ] Column sorting