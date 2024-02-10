---
title: \begin{title}\centering\vspace*{1cm}\rule{\textwidth}{0.05cm}\linebreak\vspace{0.5cm}{\huge\bfseries Messaging Website Initial Diagrams \par}\vspace{0.1cm}\hrule\end{title}
date: \today
---

# Use Case Diagram

**What normal user can do:**

1. Sign Up
2. Login
3. Send Text Message
4. Send Images
5. Search For Messages
6. Delete Messages
7. Read Message in Group Chat
8. Change Profile Picture
9. Update Profile Information (Name, Email, Password)
10. Edit Messages
11. Logout

**What admin can do:**

1. Sign Up
2. Login
3. Ban/Unban Users
4. Delete Users
5. Delete Messages
6. Update Application Content
7. View System Statistics in a Dashboard
8. Logout

```{.plantuml caption="Initial Use Case Diagram" width=30%}
@startuml
left to right direction
actor User
actor Admin

rectangle "Messaging Website" {
    User --> (Sign Up)
    User --> (Login)
    User --> (Send Text Message)
    User --> (Send Images)
    User --> (Search For Messages)
    User --> (Delete Messages)
    User --> (Read Message in Group Chat)
    User --> (Change Profile Picture)
    User --> (Update Profile Information)
    User --> (Edit Messages)
    User --> (Logout)

    Admin --> (Sign Up)
    Admin --> (Login)
    Admin --> (Ban/Unban Users)
    Admin --> (Delete Users)
    Admin --> (Delete Messages)
    Admin --> (Update Application Content)
    Admin --> (View System Statistics in a Dashboard)
    Admin --> (Logout)
}
@enduml
```

# Activity Diagram

We will need an activity diagram for each use case.

```{.plantuml caption="Initial Activity Diagram" width=30%}
@startuml
start
:User logs in;
if (Is login successful?) then (yes)
    :User is on home page;
    while (User is logged in) is (yes)
        :User sends a message;
        :User reads a message;
    endwhile (no)
else (no)
    :User tries to login again;
endif
:User logs out;
stop
@enduml
```

```{.plantuml caption="Initial Activity Diagram" width=30%}
@startuml
start
:User logs in;
if (Is login successful?) then (yes)
    :User is on home page;
    :User starts a new message;
    :User adds an attachment;
    :User sends the message;
else (no)
    :User tries to login again;
endif
:User logs out;
stop
@enduml
```

```{.plantuml caption="Initial Activity Diagram" width=30%}
@startuml
start
:Admin logs in;
if (Is login successful?) then (yes)
    :Admin is on admin dashboard;
    :Admin searches for a user;
    :Admin deletes the user;
else (no)
    :Admin tries to login again;
endif
:Admin logs out;
stop
@enduml
```

# Context & DFD

```{.mermaid caption="Initial Context Diagram" width=70%}
graph LR
  User[User] -- Send/Receive messages --> Website[Messaging Website]
  Website -- Store/Retrieve messages --> Database[Database]
  Website -- Authenticate users --> Auth[Authentication Service]
  Website -- Notify users --> Push[Push Notification Service]
  Website -- Sync messages --> Cloud[Cloud Storage Service]
```

```{.mermaid caption="Initial DFD" width=70%}
graph LR
    User(User) -->|Interacts| UM[User Management]
    UM -->|Manages| UD[User Data]
    UM -->|Manages| MM[Message Management]
    MM -->|Manages| MD[Message Data]
    UM -->|Manages| NM[Notification Management]
    NM -->|Sends Notifications| Push[Push Notification Service]
    MM -->|Syncs Messages| Cloud[Cloud Storage Service]
    UM -->|Authenticates Users| Auth[Authentication Service]
```

# Sequence Diagram

```{.plantuml caption="Initial Sequence Diagram" width=30%}
@startuml
actor User
participant "User Interface" as UI
participant "Business Logic" as BL
database "Database" as DB

User -> UI : Login
activate UI
UI -> BL : Validate User
activate BL
BL -> DB : Retrieve User Data
activate DB
DB --> BL : User Data
deactivate DB
BL --> UI : User Validated
deactivate BL
UI --> User : Access Granted
deactivate UI

User -> UI : Send Message
activate UI
UI -> BL : Process Message
activate BL
BL -> DB : Store Message
activate DB
DB --> BL : Message Stored
deactivate DB
BL --> UI : Message Sent
deactivate BL
UI --> User : Message Sent Confirmation
deactivate UI

User -> UI : Read Message
activate UI
UI -> BL : Fetch Message
activate BL
BL -> DB : Retrieve Message
activate DB
DB --> BL : Message Data
deactivate DB
BL --> UI : Display Message
deactivate BL
UI --> User : Message
deactivate UI

User -> UI : Logout
activate UI
UI -> BL : Logout User
activate BL
BL --> UI : User Logged Out
deactivate BL
UI --> User : Logout Confirmation
deactivate UI
@enduml
```

# Class Diagram

```{.plantuml caption="Initial Class Diagram" width=70%}
@startuml
class User {
  +username: String
  +password: String
  +email: String
  +login(): void
  +logout(): void
  +sendMessage(): void
  +readMessage(): void
}

class Message {
  +messageId: Integer
  +content: String
  +timestamp: Date
  +sender: User
  +receiver: User
  +send(): void
  +read(): void
}

class Group {
  +groupId: Integer
  +name: String
  +members: User[]
  +addMember(): void
  +removeMember(): void
}

class Admin extends User {
  +banUser(): void
  +unbanUser(): void
}

User "1" -- "many" Message : sends >
User "1" -- "many" Message : receives <
User "many" -- "many" Group : is in >
Admin "1" -- "many" User : manages >
@enduml
```

# State Diagram

```{.mermaid caption="Initial State Diagram" width=80%}
stateDiagram-v2
    [*] --> NotLoggedIn
    NotLoggedIn --> LoggingIn: Login
    LoggingIn --> LoggedIn: Successful Login
    LoggingIn --> NotLoggedIn: Failed Login
    LoggedIn --> ComposingMessage: Start Composing Message
    ComposingMessage --> LoggedIn: Send Message
    LoggedIn --> ReadingMessage: Open Message
    ReadingMessage --> LoggedIn: Close Message
    ReadingMessage --> ReplyingToMessage: Reply to Message
    ReplyingToMessage --> LoggedIn: Send Reply
    LoggedIn --> LoggingOut: Logout
    LoggingOut --> NotLoggedIn: Successful Logout
    LoggingOut --> LoggedIn: Failed Logout
```
