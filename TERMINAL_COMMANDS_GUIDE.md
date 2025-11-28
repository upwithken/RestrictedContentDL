# Terminal Commands Guide for Beginners

A comprehensive guide to essential terminal commands used in this CoreTrade project. Perfect for beginners!

---

## 📁 Navigation Commands

### Basic Navigation

```bash
# Show current directory (Print Working Directory)
pwd

# Change to a specific directory
cd /path/to/directory

# Change to server folder (from project root)
cd server

# Change to client folder (from project root)
cd client

# Go back to project root (from server or client folder)
cd ..

# Go up multiple directory levels
cd ../..      # Go up 2 levels
cd ../../..   # Go up 3 levels

# Go to home directory
cd ~
# or simply
cd

# Go back to previous directory
cd -
```

### Quick Navigation Examples

```bash
# From project root to server
cd server

# From server back to root
cd ..

# From root to client
cd client

# From client back to root
cd ..

# Absolute path navigation (works from anywhere)
cd /Users/lanre/Desktop/Kiyshoi/core-trade2
cd /Users/lanre/Desktop/Kiyshoi/core-trade2/server
cd /Users/lanre/Desktop/Kiyshoi/core-trade2/client
```

---

## 📋 File and Directory Commands

### Viewing Files and Directories

```bash
# List files in current directory
ls

# List files with details (permissions, size, date)
ls -l

# List all files including hidden ones (files starting with .)
ls -la

# List files in a specific directory
ls server/
ls client/

# Show first 10 lines of a file
head filename.txt

# Show last 10 lines of a file
tail filename.txt

# View entire file content
cat filename.txt

# View file with line numbers
cat -n filename.txt
```

### File Operations

```bash
# Copy a file
cp source.txt destination.txt

# Copy a file to another directory
cp file.txt server/

# Copy entire directory
cp -r source_folder destination_folder

# Move/rename a file
mv oldname.txt newname.txt

# Move file to another directory
mv file.txt server/

# Delete a file
rm filename.txt

# Delete a directory and all contents (BE CAREFUL!)
rm -r directory_name

# Create a new directory
mkdir new_folder

# Create nested directories
mkdir -p folder1/folder2/folder3
```

### Moving/Copying Multiple Files

```bash
# Move multiple files at once (list them separated by spaces)
mv file1.md file2.md file3.md destination_folder/

# Move all files matching a pattern (using wildcards)
mv z*.md instructions/
# This moves all files starting with "z" and ending with ".md"
# Example: zFORK_WORKFLOW.md, zNEXT_STEPS.md, zREADME.md

# Move files matching pattern to folder
mv *.md docs/
# Moves all .md files to docs/ folder

# Move files with any extension matching a pattern
mv z*.* folder/
# Moves all files starting with "z" regardless of extension

# Copy multiple files at once
cp file1.txt file2.txt file3.txt backup_folder/

# Copy all files matching a pattern
cp *.md backup/
cp z*.md instructions/

# Move files using brace expansion (for similar names)
mv z{NEXT_STEPS,FORK_WORKFLOW,RAILWAY_SETUP}.md instructions/
# This expands to: mv zNEXT_STEPS.md zFORK_WORKFLOW.md zRAILWAY_SETUP.md instructions/

# Check what files match before moving (safety tip!)
ls z*.md
# This shows you which files will be moved, then:
mv z*.md instructions/

# Move files to a new directory (creates directory if it doesn't exist)
mkdir -p instructions && mv z*.md instructions/
```

### Wildcard Patterns Explained

```bash
# * matches any characters (zero or more)
*.md              # All .md files
z*.md             # Files starting with "z" and ending with ".md"
*.txt             # All .txt files
test*             # Files starting with "test"

# ? matches a single character
file?.txt         # file1.txt, file2.txt (but not file10.txt)

# [ ] matches any single character in brackets
file[123].txt     # file1.txt, file2.txt, or file3.txt

# { } brace expansion (creates multiple combinations)
{file1,file2}.txt # Expands to: file1.txt file2.txt
```

### Practical Examples

```bash
# Move all documentation files to docs folder
mv *.md docs/

# Move all Python files to scripts folder
mv *.py scripts/

# Move files starting with "z" to instructions folder
mv z*.md instructions/

# Move configuration files to config folder
mv *.json *.env config/ 2>/dev/null
# The 2>/dev/null suppresses errors if some files don't exist

# Copy all backup files
cp *.bak backup_folder/

# Move all files except a specific one
mv !(dont_move.txt) destination/
# or use find:
find . -maxdepth 1 -name "*.md" ! -name "README.md" -exec mv {} docs/ \;
```

---

## 🔍 Search and Filter Commands

### Searching in Files

```bash
# Search for text in files (grep)
grep "search term" filename.txt

# Search case-insensitive
grep -i "search term" filename.txt

# Search in all files in current directory
grep -r "search term" .

# Search in specific directory
grep -r "PORT" server/

# Count occurrences
grep -c "search term" filename.txt

# Show line numbers
grep -n "search term" filename.txt
```

### Finding Files

```bash
# Find files by name
find . -name "*.js"

# Find files in specific directory
find server -name "*.js"

# Find directories
find . -type d -name "node_modules"
```

---

## 🌐 Network and Port Commands

### Checking Ports

```bash
# Check what's using a specific port
lsof -i :3000
lsof -i :8000
lsof -i :5000

# List all listening ports
lsof -i -P -n | grep LISTEN

# Check if a port is available
lsof -i :PORT_NUMBER
# If nothing shows up, the port is free!

# Show only port numbers in use
lsof -i -P -n | grep LISTEN | awk '{print $9}' | cut -d: -f2 | sort -n | uniq
```

### Testing API Endpoints

```bash
# Test if server is responding
curl http://localhost:8000/api/health

# Test with more details
curl -v http://localhost:8000/api/health

# Test POST request
curl -X POST http://localhost:8000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","password":"test123"}'
```

---

## 🔧 Process Management

### Viewing Processes

```bash
# List all node processes
ps aux | grep node

# List processes using a specific port
lsof -i :8000

# Find process by name
ps aux | grep "server.js"
```

### Killing Processes

```bash
# Kill a process by PID (Process ID)
kill PID_NUMBER

# Force kill a process
kill -9 PID_NUMBER

# Kill all processes matching a pattern
pkill -f "node.*server.js"

# Kill all node processes (BE CAREFUL!)
pkill node
```

### Finding Process IDs

```bash
# Find PID of process using a port
lsof -ti :8000

# Kill process using a port
kill $(lsof -ti :8000)
```

---

## 📦 NPM Commands

### Installation

```bash
# Install dependencies in current directory
npm install

# Install all dependencies (root, server, and client)
npm run install-all

# Install specific package
npm install package-name

# Install as development dependency
npm install --save-dev package-name
```

### Running Scripts

```bash
# Run development mode (both server and client)
npm run dev

# Run server only
npm run server
# or
cd server && npm run dev

# Run client only
npm run client
# or
cd client && npm run dev

# Build for production
npm run build

# Start production server
npm start
```

### Package Management

```bash
# List installed packages
npm list

# Check for outdated packages
npm outdated

# Update packages
npm update

# Remove a package
npm uninstall package-name
```

---

## 🔐 Environment Variables

### Viewing Environment Variables

```bash
# View all environment variables
env

# View specific variable
echo $PATH
echo $HOME

# Check if variable is set
echo $PORT
```

### Working with .env Files

```bash
# View .env file (if not in .gitignore)
cat server/.env

# Check if variable exists in .env
grep "PORT" server/.env

# Add line to .env file
echo "NEW_VAR=value" >> server/.env

# Edit .env file (opens in default editor)
open server/.env        # macOS
nano server/.env        # Linux/macOS (terminal editor)
vim server/.env         # Advanced editor
```

---

## 🛠️ Text Editing Commands

### Using sed (Stream Editor)

```bash
# Replace text in a file
sed -i '' 's/old-text/new-text/' filename.txt

# Replace in .env file (macOS)
sed -i '' 's/^PORT=3000/PORT=8000/' server/.env

# Replace all occurrences
sed -i '' 's/old/new/g' filename.txt

# Add line at end of file
echo "NEW_LINE" >> filename.txt
```

### Using cat for File Operations

```bash
# Create a new file with content
cat > newfile.txt << EOF
Line 1
Line 2
EOF

# Append to file
cat >> existingfile.txt << EOF
New line
EOF
```

---

## 🗄️ Database Commands

### MongoDB

```bash
# Check if MongoDB is running
lsof -i :27017

# Connect to MongoDB (if installed)
mongosh

# Connect to specific database
mongosh mongodb://localhost:27017/coretrade
```

---

## 🐛 Debugging Commands

### Checking Server Status

```bash
# Check if server is running on port 8000
lsof -i :8000

# Test server health endpoint
curl http://localhost:8000/api/health

# Check server logs (if running in terminal)
# Just look at the terminal where server is running
```

### Common Debugging

```bash
# Check Node.js version
node --version
# or
node -v

# Check npm version
npm --version
# or
npm -v

# Check which node is being used
which node

# Check npm global packages location
npm root -g
```

---

## 📊 Useful Command Combinations

### Check Multiple Ports at Once

```bash
for port in 3000 3001 5000 8000; do
  lsof -i :$port > /dev/null 2>&1 && echo "Port $port: IN USE" || echo "Port $port: AVAILABLE"
done
```

### Find and Kill Process on Port

```bash
# One-liner to kill process on port 8000
lsof -ti :8000 | xargs kill -9
```

### Check File Permissions

```bash
# View file permissions
ls -l filename.txt

# Make file executable
chmod +x script.sh

# Change file ownership (usually requires sudo)
sudo chown username:group filename.txt
```

---

## 🚀 Project-Specific Commands

### Starting the Project

```bash
# From project root - start both server and client
npm run dev

# Start only server (from root)
npm run server

# Start only client (from root)
npm run client

# Start server manually
cd server && npm run dev

# Start client manually
cd client && npm run dev
```

### Building the Project

```bash
# Build client for production
npm run build

# Start production server
npm start
```

### Environment Setup

```bash
# Copy environment example to .env
cp server/ENV.example server/.env

# Check environment variables
cat server/.env

# Edit environment file
nano server/.env
```

---

## 💡 Pro Tips for Beginners

### 1. Always Know Where You Are
```bash
pwd  # Run this often to check your location
```

### 2. Use Tab Completion
- Press `Tab` to auto-complete file/directory names
- Saves typing and prevents typos!

### 3. Use Arrow Keys
- `↑` (Up arrow) - Previous command
- `↓` (Down arrow) - Next command
- `←` `→` - Move cursor left/right

### 4. Clear the Screen
```bash
clear
# or press Ctrl+L
```

### 5. Cancel a Running Command
```bash
# Press Ctrl+C to stop a running process
```

### 6. Get Help
```bash
# Get help for any command
man command_name
command_name --help
```

### 7. Chain Commands
```bash
# Run multiple commands in sequence
cd server && npm run dev

# Run second command only if first succeeds
cd server && npm install

# Run second command regardless
cd server; npm install
```

### 8. View Command History
```bash
# View all previous commands
history

# Search history (press Ctrl+R)
# Then type to search
```

### 9. Check Files Before Moving Multiple Files
```bash
# Always check what files match before moving them
ls z*.md              # See which files match the pattern
mv z*.md folder/      # Then move them

# This prevents accidentally moving wrong files!
# You can also use wildcards with ls to preview:
ls *.md               # See all .md files before moving
ls z*.md              # See all files starting with "z" and ending with ".md"
```

---

## ⚠️ Important Safety Tips

1. **Always check before deleting**: Use `ls` to see files before `rm`
2. **Check files before moving multiple files**: Use `ls *.md` to preview what matches before `mv *.md folder/`
3. **Be careful with `rm -r`**: This deletes directories permanently
4. **Don't run `sudo` commands unless you understand them**: They have admin privileges
5. **Check ports before killing processes**: Make sure you're killing the right thing
6. **Backup important files**: Before making changes, copy files first
7. **Test wildcard patterns first**: Use `ls pattern*` before `mv pattern* folder/` to see what will be affected

---

## 📚 Additional Resources

- **Learn more about terminal**: Search for "bash tutorial" or "terminal basics"
- **Command help**: Most commands support `--help` flag
- **Manual pages**: Use `man command_name` for detailed documentation

---

## 🎯 Quick Reference Cheat Sheet

```bash
# Navigation
pwd                    # Where am I?
cd folder              # Go to folder
cd ..                  # Go back
cd ~                   # Go home

# Files
ls                     # List files
cat file.txt           # View file
cp file1 file2         # Copy
mv file1 file2         # Move/rename
rm file.txt            # Delete
mv *.md folder/        # Move multiple files (wildcards)
mv z*.md folder/       # Move files matching pattern
cp *.txt backup/       # Copy multiple files
ls *.md                # List files matching pattern

# Search
grep "text" file.txt   # Find text
find . -name "*.js"    # Find files

# Ports
lsof -i :8000          # Check port
lsof -i -P -n | grep LISTEN  # All ports

# Processes
ps aux | grep node     # Find processes
kill PID               # Kill process
pkill -f "pattern"     # Kill by pattern

# NPM
npm install            # Install packages
npm run dev            # Run dev server
npm run build          # Build project

# Project
npm run dev            # Start everything
npm run server         # Server only
npm run client         # Client only
```

---

**Remember**: Practice makes perfect! Don't be afraid to experiment (safely) and learn by doing. 🚀

