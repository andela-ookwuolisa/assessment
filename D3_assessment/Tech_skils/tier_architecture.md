 # 2&3 tier architecture
 
 ## Expectation
 The Developer has a thorough understanding of multi-tier architecture and is able to guide a team in the intricacies of its development.

 ## justification
 Multitier architecture (often referred to as n-tier architecture) or multilayered architecture is a client-server architecture in which presentation, application processing, and data management functions are physically separated. 

 - Presentation layer
This is the topmost level of the application. The presentation tier displays information related to such services as browsing merchandise, purchasing and shopping cart contents. It communicates with other tiers by which it puts out the results to the browser/client tier and all other tiers in the network. In simple terms, it is a layer which users can access directly (such as a web page, or an operating system's GUI).

- Application layer (business logic, logic tier, or middle tier)
The logical tier is pulled out from the presentation tier and, as its own layer, it controls an application’s functionality by performing detailed processing.

- Data Layer
The data tier includes the data persistence mechanisms (database servers, file shares, etc.) and the data access layer that encapsulates the persistence mechanisms and exposes the data. The data access layer should provide an API to the application tier that exposes methods of managing the stored data without exposing or creating dependencies on the data storage mechanisms.


 ### One tier architecture
 In one-tier architectures, the presentation, application, and data layer are all in one physical system. E.g Personal computers. MP3 players, MS office, etc are one-tier applications.

### Two-tier architecture
The two-tier architecture is similar to a basic client-server model. The application at the client end directly communicates with the database at the server side. The server side is responsible for providing query processing. On the client side, the user interfaces and application programs are run.
An advantage of this type is that maintenance and understanding are easier, compatible with existing systems. However, this model gives poor performance when there are a large number of users.
If the application architecture has no explicit distinction between the business layer and the presentation layer (i.e., the presentation layer is considered part of the business layer), then a traditional client-server (two-tier) model has been implemented. E.g Database APIs

### Three-tier architecture
Three-tier architecture is a software architecture pattern in which the presentation layer, application layer, and data storage layer are developed and maintained as independent modules, on separate platforms. In this architecture, there is a clear distinction between the client, application and database layer. E.g Web apps.
