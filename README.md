# Ohjelmistotekniikka, harjoitustyö

### Exercises and project for the course "Intermediate Studies Project: Software Development Methods" - University of Helsinki
## Depysit

This software is made for tracking personal finances, while providing a nice view of incomes - expenses to help with budgeting.
Multiple users are supported, so this would work great in a family setting for example.

### Documentation

- [Guide](./documentation/guide.md)
- [Requirement specification](./documentation/requirement%20specification.md)
- [Record of working hours](./documentation/record%20of%20working%20hours.md)
- [Changelog](./documentation/changelog.md)
- [Architecture](./documentation/architecture.md)
- [Testing](./documentation/tests.md)

### Installation

1. Install dependencies with:

```
poetry install
```

2. Create a .env file in root with the following contents: (Optional)

```
DATABASE_NAME="NAME HERE"
```

3. Start the program with:

```
poetry run invoke start
```

### Command line commands

Run the program with:

```
poetry run invoke start
```

Run tests with:

```
poetry run invoke test
```

Generate coverage:

```
poetry run invoke coverage-report
```

Run pylint:

```
poetry run invoke lint
```