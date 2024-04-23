### Structure

```mermaid
classDiagram
entities <|-- repositories
entities <|-- services
repositories <|-- services
services <|-- gui

entities: Base
entities: User
entities: Entry

repositories: UserRepository
repositories: EntryRepository

services: UserService
services: EntryService

gui: MainWindow
gui: ComboForm
gui: EntryForm
```

This is roughly how the different areas of the code interact with eachother. Note that this is not a standard class
diagram!

### Main functionalities
#### User registration

```mermaid
sequenceDiagram
    actor User
    participant GUI
    participant UserService
    participant UserRepository
    participant example
    User ->> GUI: click "Register" button
    GUI ->> UserService: register("example", "example")
    UserService ->> UserRepository: find_user_name("example")
    UserRepository -->> UserService: user
    UserService ->> example: User("example", "example")
    UserService ->> UserRepository: add_user(example)
    UserRepository -->> UserService: None
    UserService -->> GUI: user.id
```