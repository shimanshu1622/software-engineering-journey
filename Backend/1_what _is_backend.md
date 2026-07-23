## 1. What is Backend?
- A backend is a server (computer) that listens for client requets over the internet and processes them.
- It typically listens on ports such as:
```
HTTP -> Port 80
HTTPS -> Port 443
WebSocket
gRPS
```
- Clients (browser, mobile app, frontend) sends requests to the backend, and the backend returns a response.

## 2. What does a backend do?
- A backend can:
```
Serve HTML pages
Serve CSS & JS files
Serve Images
Return JSON data
Accept user data
Process requests
Store data in databases
Authenticate users
perform business logic
```

## 3. Backend request flow
```
Browser
    |
    v
Domain Name
    |
    v
DNS server
    |
    v
public IP address
    |
    v
AWS firewall (security group)
    |
    v
EC2 instance (backend server)
    |
    v
Nginx (Reverse proxy)
    |
    v
Backend application (Node.js, Python, Java, etc.)
    |
    v
Databse/Business logic
    |
    v
response
    |
    v
Browser
```
> This is the complete journey of a HTTP request from browser to the backend server.

### DNS (Domain Name System)
- DNS converts a human readable domain name into an IP address.
``` 
backend.exp.com  --> 43.204.xx.xx
```

### AWS EC2
- EC2 is simply a virtual computer running in AWS cloud.
- It has : CPU, RAM, Storage, OS, Public IP
- Your backend application runs inside this machine.

### Security Group(Firewall)
- Before a request reaches the server, it passes through AWS security groups

### Reverse Proxy (Nginx)
- Ngnix sits in front of your backend server.
```
Client --> Ngnix --> Node.js
```
**Purpose**
- Route requests
- SSL termination
- Redirect HTTP -> HTTPS
- Handle multiple applications
- Load balancing 

> your backend usually runs on: localhost: 3001\
> The browser cannot access this directly over the internet\
> Ngnix forwards public requests to this local port.

## 4. Why do we Need a Backend?
**Exp**
```
Instagram like
User Like
    |
    v
Frontend sends request
    |
    v
backend verifies user
    |
    v
Stores like in database
    |
    v
finds post owner
    |
    v
Sends notification
    |
    v
Friend receives notification
```
> without a backend, there is no centralized place tp store or process the information.

## 5. Main resposibility of backend
- the backend primary resposibility in one word: `DATA`
```
Receive data
fetch data
validate data
store data
update data
delete data
```
> Everything revolves around data.

**A backend typically performs:**
```
Authentication
Authorization
CRUD operations
Database communication
Business logic
File upload
Logging
Notification
API integration
security checks
```

## 6. Why can't we do everything in the frontend?
- Although the frontend is also a computer, it has important limitations.

> Reason 1: Security
- Frontend javascript runs inside the user's browser.
- if browser allowed unrestricted access, websites could:
    - read local files
    - steal passwords
    - access the oS
    - upload private documents
- to prevent this, browsers run inside a `Sandbox`.

> Reason 2: Browser Sandbox
- The browser only allows to limited resources:
    - DOM
    - local storage
    - cookies
    - browser APIs
- It cannot freely access:
    - File System
    - Environment variables
    - Operating System
    - Native processes

> Reason 3: CORS
- Browser blocks requests to different domains unless the server explicitly allows them.\
**exp**\
Frontend: `frontend.com`, Tryling to call `api.otherdomin.com`, Browser blocks it because of CORS unless proper HTTP headers are configured.

> Reason 4: Database Access
- Browsers are not designed to connect directly to databases.
- backend servers use native database drivers such as:
    - PostgreSQL
    - MongoDB driver
- They also maintain connection pools for efficient database communication.
- if every browser opened its own database connection, the database would be overwhelmed.

> Reason 5: Computing Power
- Backend Servers can be upgraded easily: more RAM, powerful CPU, better hardware
- Frontend device vary: old phones, tablets, low-end laptops, slow desktops.
- **Heavy business logic should therefore run on backend server rather than client devices.**

## 7. How Frontend works
- Frontend request flow
```
  Browser
    |
    v
   DNS
    |
    v
   AWS
    |
    v
  Nginx
    |
    v
Next.js server
    |
    v
   HTML
    |
    v
   CSS
    |
    v
javascript
    |
    v
browser executes JS
    |
    v
User Interface
```
> unlike backend code, frontend js is downloaded and executed inside the user's browser.

## 8. Backend vs Frontend
|Backend | Frontend |
|--------|----------|
|Runs on server | Runs in browser |
|Executes business logic | Renders UI |
|Connects to databases | Displays data |
|Handles authentication | Collects user input |
|Stores data | Shows data |
|Returns JSON | Consumes JSON |

# Summary

- Backend = Server + Business Logic + Database + APIs
- Request Flow: Browser → DNS → Firewall → EC2 → Nginx → Backend → Database → Response
- DNS maps domain names to IP addresses.
- EC2 is the cloud server where the backend runs.
- Security Groups control which ports are accessible.
- Nginx is a reverse proxy that forwards requests to the backend.
- PM2 keeps Node.js applications running.
- The backend's primary job is to receive, process, store, and return data.
- Browsers are sandboxed, so they cannot safely replace backend servers.
- Heavy computation, database access, and sensitive logic belong on the backend.