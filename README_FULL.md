# NQCC Source Code Documentation

This directory contains the complete source code for the **NQCC (Not Quite C Compiler)** implementation in Gleam. The compiler follows a traditional multi-stage architecture with clear separation of concerns between each compilation phase.  

The updated version now supports **arithmetic operators (`+`, `-`, `*`, `/`)** and **assignment (`=`)** in addition to the original functionality of parsing and compiling very simple C-like programs.

##  Module Overview

```
src/
├── nqcc.gleam          # Main entry point and compilation driver
├── cli.gleam           # Command-line interface and argument parsing
├── compiler.gleam      # Core compilation pipeline orchestration
├── lexer.gleam         # Lexical analysis (source → tokens)
├── parser.gleam        # Syntax analysis (tokens → AST)
├── codegen.gleam       # Code generation (AST → assembly)
├── emitter.gleam       # Assembly emission (assembly → platform-specific text)
├── tokens.gleam        # Token type definitions and lexical patterns
├── ast.gleam           # Abstract Syntax Tree type definitions
├── assembly.gleam      # Assembly instruction type definitions
├── settings.gleam      # Compilation settings and platform configuration
└── utils.gleam         # Shared utility functions
```

##  Data Flow Architecture

The compiler follows a **linear transformation pipeline** where each stage consumes the output of the previous stage:

```
Source Code (String)
       ↓ lexer.gleam
   Tokens (List(Token))
       ↓ parser.gleam
   AST (Program)
       ↓ codegen.gleam
   Assembly (Assembly)
       ↓ emitter.gleam
   Assembly Text (String)
```

##  Module Details

### 1. Entry Point and Orchestration

#### `nqcc.gleam` - Main Entry Point
**Purpose**: Application bootstrap and high-level compilation driver.

**Key Functions**:
- `main()` - Application entry point, sets up CLI.
- `handle_command(Config)` - Command handler with error reporting.
- `run_driver(Config)` - Main compilation pipeline orchestration.
- `preprocess(String)` - C preprocessor integration.
- `assemble_and_link(String, Bool)` - Final assembly and linking.

**Responsibilities**:
- Application lifecycle management.  
- Integration with external tools (GCC preprocessor/assembler).  
- Resource management and cleanup.  
- High-level error handling and user messaging.  

---

#### `cli.gleam` - Command-Line Interface
**Purpose**: Command-line argument parsing and configuration management.

**Key Types**:
```gleam
pub type Config {
  Config(
    stage: settings.Stage,
    platform: settings.Platform,
    debug: Bool,
    src_file: String,
  )
}
```

**Key Functions**:
- `create_app(fn(Config) -> Nil)` - CLI application setup.  
- `run_app(glint.Glint(Nil))` - Execute CLI with system arguments.  
- `parse_config(...)` - Convert CLI flags to structured configuration.  

**Responsibilities**:
- Flag parsing and validation.  
- Help message generation.  
- Configuration structure creation.  
- CLI error handling.  

---

#### `compiler.gleam` - Compilation Pipeline
**Purpose**: Core compilation pipeline that orchestrates all compilation stages.

**Key Types**:
```gleam
pub type CompileError {
  LexError(lexer.LexError)
  ParseError(parser.ParseError)
  EmitError(String)
  IOError(String)
}
```

**Key Functions**:
- `compile(Stage, String, Platform)` - Main compilation entry point.  
- `compile_to_tokens(String)` - Lexical analysis stage.  
- `compile_to_ast(String)` - Syntax analysis stage.  
- `compile_to_asm(String)` - Code generation stage.  

**Responsibilities**:
- Stage-based compilation control.  
- Error type unification across stages.  
- Pipeline composition and data flow.  
- Early exit for debugging stages.  

---

### 2. Compilation Stages

#### `lexer.gleam` - Lexical Analysis
**Purpose**: Convert source code strings into structured token sequences.  

**Key Types**:
```gleam
pub type LexError {
  LexError(String)
}

pub type MatchDef {
  MatchDef(matched_substring: String, matching_token: TokenDef)
}
```

**Key Functions**:
- `lex(String)` - Main lexical analysis entry point.  
- `lex_recursive(String, List(TokenDef))` - Core recursive lexing algorithm.  
- `token_defs()` - Token pattern definitions.  

**Algorithm**:
1. Initialize regex-based token definitions.  
2. Recursively match patterns at current position.  
3. Use longest-match disambiguation for overlapping patterns.  
4. Convert matched text to appropriate token types.  
5. Handle whitespace and advance through input.  

**Responsibilities**:
- Pattern matching with regular expressions.  
- Keyword vs identifier disambiguation.  
- Whitespace handling and normalization.  
- Lexical error detection and reporting.  

**New Features**:
- Support for arithmetic and assignment operators:
  - `Plus` (`+`)  
  - `Minus` (`-`)  
  - `Star` (`*`)  
  - `Slash` (`/`)  
  - `Equal` (`=`)  

---

#### `parser.gleam` - Syntax Analysis
**Purpose**: Convert token streams into Abstract Syntax Trees (AST).  

**Key Types**:
```gleam
pub type ParseError {
  ParseError(String)
  UnexpectedEndOfInput
}

pub type TokenStream {
  TokenStream(tokens: List(Token), position: Int)
}
```

**Key Functions**:
- `parse(List(Token))` - Main parsing entry point.  
- `parse_program(TokenStream)` - Top-level program parsing.  
- `parse_function_definition(TokenStream)` - Function parsing.  
- `parse_statement(TokenStream)` - Statement parsing.  
- `parse_expression(TokenStream)` - Expression parsing with operator precedence.  

**Algorithm**:
- Recursive descent parser matching C grammar subset.  
- Operator precedence parsing for `+`, `-`, `*`, `/`, and `=`.  
- Top-down parsing with explicit lookahead.  
- Immutable token stream with position tracking.  
- Comprehensive error reporting with context.  

**Responsibilities**:
- Grammar rule enforcement.  
- AST node construction for arithmetic and assignments.  
- Syntax error detection and reporting.  
- Token consumption and stream management.  

**Operator Precedence Table**:
```
Highest
    *   /        (multiplication, division)
    +   -        (addition, subtraction)
    =            (assignment)
Lowest
```

---

#### `codegen.gleam` - Code Generation
**Purpose**: Transform Abstract Syntax Trees into assembly instruction sequences.  

**Key Functions**:
- `generate(ast.Program)` - Main code generation entry point.  
- `convert_function(ast.FunctionDefinition)` - Function code generation.  
- `convert_statement(ast.Statement)` - Statement code generation.  
- `convert_expression(ast.Expression)` - Expression code generation with arithmetic and assignments.  

**Code Generation Strategy**:
- Direct AST-to-assembly translation.  
- Single-pass generation (no optimization).  
- Platform-independent abstract assembly.  
- Instruction patterns extended:
  - `add`, `sub`, `imul`, `idiv` for arithmetic.  
  - `mov` for assignments.  
  - `ret` for returns.  

**Responsibilities**:
- AST traversal and transformation.  
- Instruction sequence generation.  
- Operand type selection (immediate vs register).  
- Abstract assembly construction.  

---

### 3. Type Definitions

#### `tokens.gleam` - Token Types
**Purpose**: Define all lexical units recognized by the compiler.  

**Key Types**:
```gleam
pub type Token {
  Identifier(String)
  Constant(Int)
  KWInt
  KWReturn
  KWVoid
  OpenParen
  CloseParen
  OpenBrace
  CloseBrace
  Semicolon
  Plus
  Minus
  Star
  Slash
  Equal
}

pub type TokenDef {
  TokenDef(re: regexp.Regexp, converter: fn(String) -> Token)
}
```

---

#### `ast.gleam` - Abstract Syntax Tree
**Purpose**: Define the structural representation of parsed C programs.  

**Key Types**:
```gleam
pub type Operator {
  Add
  Sub
  Mul
  Div
  Assign
}

pub type Expression {
  Constant(Int)
  Binary(Operator, Expression, Expression)
  Assign(String, Expression)
}

pub type Statement {
  Return(Expression)
}

pub type FunctionDefinition {
  Function(name: String, body: Statement)
}

pub type Program {
  Program(FunctionDefinition)
}
```

---

##  Testing Strategy

**Examples of Supported Programs**:

### Example 1: Simple Arithmetic
```c
int main(void) {
    return 1 + 2 * 3;
}
```

**AST**:
```
Program
  Function: main
    Return
      Binary(Add)
        Constant: 1
        Binary(Mul)
          Constant: 2
          Constant: 3
```

**Assembly**:
```asm
mov eax, 2
imul eax, 3
add eax, 1
ret
```

---

### Example 2: Assignment + Return
```c
int main(void) {
    x = 4 + 5;
    return x;
}
```

**AST**:
```
Program
  Function: main
    Assign(x)
      Binary(Add)
        Constant: 4
        Constant: 5
    Return
      Identifier: x
```

**Assembly**:
```asm
mov eax, 4
add eax, 5
mov [x], eax
mov eax, [x]
ret
```

---

### Example 3: Mixed Operations
```c
int main(void) {
    return (10 - 3) / 7;
}
```

**AST**:
```
Program
  Function: main
    Return
      Binary(Div)
        Binary(Sub)
          Constant: 10
          Constant: 3
        Constant: 7
```

**Assembly**:
```asm
mov eax, 10
sub eax, 3
mov ebx, 7
idiv ebx
ret
```

---

##  Error Handling

- Unexpected tokens produce descriptive errors like:  
  ```
  ParseError: Expected ";" but found "}"
  ```
- End-of-input errors are clearly distinguished:  
  ```
  UnexpectedEndOfInput: missing closing brace
  ```

---

##  Design Rationale

- Keep modules small and cohesive.  
- Support incremental language growth.  
- Maintain clear separation between **tokens**, **AST**, **parsing**, and **codegen**.  
- Write tests for each stage independently.  

---

##  Future Work

- Add support for variables and symbol tables.  
- Add type checking (int, float, char).  
- Implement comparison operators (`<`, `>`, `==`, etc.).  
- Add conditional statements (`if`, `else`).  
- Add loops (`while`, `for`).  
- Expand assignment to include compound operators (`+=`, `-=`, etc.).  
- Improve assembly generation with register allocation.  
- Support multiple functions per program.  

---

✅ 
