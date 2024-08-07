NEW_TESTS_TOKENIZER = [

    ["""p0
  (/* This is a comment // but that is not a new one!
// this one should not remove the end of the previous one*/
    F2 L
  )2 (
    F2 R
  )2
q

(
  P0
)2""",
     ["p0", "(", "F2", "L", ")2", "(", "F2", "R", ")2", "q", "(", "P0", ")2"],
     ""],

    ["""p0
  (// This is a comment /* but that is not a multiline one!
    F2 L
  )2 (
    F2 R
  )2
// this end of multiline comment doesn't 'exist'*/
q

(
  P0
)2""",
     ["p0", "(", "F2", "L", ")2", "(", "F2", "R", ")2", "q", "(", "P0", ")2"],
     ""],

    ["""p0
  (/* This is a comment // but that is not! */
// */ this shouldn't fail because this is a comment too
    F2 L
  )2 (
    F2 R
  )2
q

(
  P0
)2""",
     ["p0", "(", "F2", "L", ")2", "(", "F2", "R", ")2", "q", "(", "P0", ")2"],
     ""],

    # shouldn't raise on invalid syntaxes that are in comments
    ["""p0
  (//FFR(L3
    F2 L
  )2 (
    F2 R
  )2
q
/*p0FFFq*/
(
  P0
)2""",
     ["p0", "(", "F2", "L", ")2", "(", "F2", "R", ")2", "q", "(", "P0", ")2"],
     ""],

    # should work with single line coment symbol within a single line comment too
    ["""p0
  (//FFR ( // this should be erased successfully too
    F2 L
  )2 (
    F2 R
  )2
q
(
  P0
)2""",
     ["p0", "(", "F2", "L", ")2", "(", "F2", "R", ")2", "q", "(", "P0", ")2"],
     ""],

]

NEW_TESTS_COMPILER = [

    ["""p0
    F2 R F4 L
P0""",
     None,
     "An error should be thrown at the converter if pattern definition isn't closed"],

    ["p31(L7LFFLF5FL9F5(R9F4FR)R1qL9FF5(FF)7Rp186FRqR8LF",
     None,
     "An error should be thrown at the converter if a bracket isn't closed properly, while inside a pattern definition"],

    ["p31L7LFFLF5FL9)F5(R9F4FR)R1qL9FF5(FF)7Rp186FRqR8LF",
     None,
     "An error should be thrown at the converter if a bracket isn't opened properly, while inside a pattern definition"],

    ["""FR2p96LLF6qFLL7P96P96P96p96LRR8R1//R7LPp96L5FR7
RF4F7F3qRL((F(LF4())F7/*L8F1L1L7Pp96PF7PF2RFR()4()4*/R2)R)//L8FFF
R3""",
     None,
     "Should throw an error when 2 patterns are defined with the same name at the root level"],

    ["""
(P626)3
p626
    RR
    p968
        P919
    q
    (P968)0     // <<< cCheck this!!
q""",
     ["R", "R", "R", "R", "R", "R"],
     "Program shouldn't fail because of an invalid "],

    ["""F(P7)0
    p7
        RLRL1L6FL2
        P7
        F1(R3(R2LFR)FL)9R
    q
    LF7RRF""",
     ["F", "L", "F", "F", "F", "F", "F", "F", "F", "R", "R", "F"],
     "A \"would be\" infinite loop that is never triggered shouldn't fail."],

]

TESTS_THE_TOKENIZER1 = [

    # Example RS3-compliant program from the Story
    ["p0FFLFFR((FFFR)2(FFFFFL)3)4qp1FRqp2FP1qp3FP2qp4FP3qP0P1P2P3P4",
     ["p0", "F", "F", "L", "F", "F", "R", "(", "(", "F", "F", "F", "R", ")2", "(", "F", "F", "F", "F", "F", "L", ")3",
      ")4", "q", "p1", "F", "R", "q", "p2", "F", "P1", "q", "p3", "F", "P2", "q", "p4", "F", "P3", "q", "P0", "P1",
      "P2", "P3", "P4"],
     ""],

    # RSU Official Specs - Whitespace and Indentation Support - Example 1
    ["""p0
  (
    F2 L
  )2 (
    F2 R
  )2
q

(
  P0
)2""",
     ["p0", "(", "F2", "L", ")2", "(", "F2", "R", ")2", "q", "(", "P0", ")2"],
     ""],

    # RSU Official Specs - Comment Support - Code Example
    ["""/*
  RoboScript Ultimatum (RSU)
  A simple and comprehensive code example
*/

// Define a new pattern with identifier n = 0
p0
  // The commands below causes the MyRobot to move
  // in a short snake-like path upwards if executed
  (
    F2 L // Go forwards two steps and then turn left
  )2 (
    F2 R // Go forwards two steps and then turn right
  )2
q

// Execute the snake-like pattern twice to generate
// a longer snake-like pattern
(
  P0
)2""",
     ["p0", "(", "F2", "L", ")2", "(", "F2", "R", ")2", "q", "(", "P0", ")2"], ""],

    # RSU Official Specs - Pattern Scoping - Example 1
    ["""// The global scope can "see" P1 and P2
p1
  // P1 can see P2, P3 and P4
  p3
    // P3 can see P1, P2 and P4 though invoking
    // P1 will likely result in infinite recursion
    F L
  q
  p4
    // Similar rules apply to P4 as they do in P3
    F P3
  q

  F P4
q
p2
  // P2 can "see" P1 and therefore can invoke P1 if it wishes
  F3 R
q

(
  P1 P2
)2 // Execute both globally defined patterns twice""",
     ["p1", "p3", "F", "L", "q", "p4", "F", "P3", "q", "F", "P4", "q", "p2", "F3", "R", "q", "(", "P1", "P2", ")2"],
     ""],

    # RSU Official Specs - Pattern Scoping - Example 2
    ["""p1
  p1
    F R
  q

  F2 P1 // Refers to "inner" (locally defined) P1 so no infinite recursion results
q

(
  F2 P1 // Refers to "outer" (global) P1 since the
  // global scope can"t "see" local P1
)4

/*
  Equivalent to executing the following raw commands:
  F F F F F R F F F F F R F F F F F R F F F F F R
*/""",
     ["p1", "p1", "F", "R", "q", "F2", "P1", "q", "(", "F2", "P1", ")4"], ""],

    # Edge Assertions - Weird and Empty Comments
    ["""/*RoboScript Ultimatum (RSU)A simple and comprehensive code example*///Define a new pattern with identifier n = 0
p0//The commands below causes the MyRobot to move
//in a short snake-like path upwards if executed
(F2L// Go forwards two steps and then turn left
)2(F2R// Go forwards two steps and then turn right
)2q//Execute the snake-like pattern twice to generate
//a longer snake-like pattern
(P0)2""",
     ["p0", "(", "F2", "L", ")2", "(", "F2", "R", ")2", "q", "(", "P0", ")2"], ""],

    ["""/**///
p0////
(F2L//
)2(F2R//\r\r\r\r\r                   \r\r\r\r\r
)2q//
(P0)2""",
     ["p0", "(", "F2", "L", ")2", "(", "F2", "R", ")2", "q", "(", "P0", ")2"], ""],

    # Edge Assertions - Weird but valid indentation
    ["""p0
                         \r\r\r            (
 F2   L
)2                                                       (
                                        F2R                                )2
q        (
                                                                     P0
)2                              \r\r\r\r\r\r\r\r\r\r""",
     ["p0", "(", "F2", "L", ")2", "(", "F2", "R", ")2", "q", "(", "P0", ")2"], ""],

    # Edge Assertions - All possible token forms in one program
    ["""
p0
  (
    F2 L F L F0 R F5 R
  )
  (
    (
      F L2 R3 R0 L4 L0 R5 F6
    )7
    (
      F7 F9 L L4 L R2 R R9
    )4
  )9
  ()0
q

(
  P0 P0 P0
)""",
     ["p0", "(", "F2", "L", "F", "L", "F0", "R", "F5", "R", ")", "(", "(", "F", "L2", "R3", "R0", "L4", "L0", "R5",
      "F6", ")7", "(", "F7", "F9", "L", "L4", "L", "R2", "R", "R9", ")4", ")9", "(", ")0", "q", "(", "P0", "P0", "P0",
      ")"], ""],

    # Edge Assertions - Multi-digit integers
    ["""
p3407
  (
    F242 L F L F57 R F15 R
  )
  (
    (
      F L3324 R3 L4 R665 F6
    )79
    (
      F7 F9 L L4 L R2 R R9
    )48
  )9899000
q

(
  P3407 P3407 P3407
)""",
     ["p3407", "(", "F242", "L", "F", "L", "F57", "R", "F15", "R", ")", "(", "(", "F", "L3324", "R3", "L4", "R665",
      "F6", ")79", "(", "F7", "F9", "L", "L4", "L", "R2", "R", "R9", ")48", ")9899000", "q", "(", "P3407", "P3407",
      "P3407", ")"], ""],

]

# ***************************************************************


TESTS_THE_TOKENIZER2 = [

    # RSU Official Specs - Whitespace and Indentation Support - Example 2
    ["""p 0
  (
    F 2L
  ) 2 (
    F 2 R
  )         2
q

(
  P  0
)2""",
     None,
     "Your tokenizer should throw an error whenever there is whitespace before numbers (stray numbers)"],

    # RSU Official Specs - Finally ... - Mini Code Example 1
    [
        """this is a stray comment not escaped by a double slash or slash followed by asterisk F F F L F F F R F F F L F F F R and lowercase "flr" are not acceptable as commands""",
        None,
        "Your tokenizer should throw an error when there are \"stray comments\""],

    # RSU Official Specs - Finally ... - Mini Code Example 2
    ["""F 32R 298984""",
     None,
     "Your tokenizer should throw an error in the presence of \"stray numbers\""],

    # Edge Assertions - Leading Zeroes
    ["""p03
  (
    F4 L
  )4
q

P03""",
     None,
     "Your tokenizer should not allow integer postfixes with leading zeroes"],

    ["""p3
  (
    F4 L F00
  )4
q

P3""",
     None,
     "Your tokenizer should not allow integer postfixes with leading zeroes"],

    ["""p3
  (
    F4 L0001
  )4
q

P3""",
     None,
     "Your tokenizer should not allow integer postfixes with leading zeroes"],

    ["""p3
  (
    F4 L1
  )004
q

P3""",
     None,
     "Your tokenizer should not allow integer postfixes with leading zeroes"],

    # Edge Assertions - Unidentified Pattern
    ["""p
  (
    F4 L
  )4
q

P3""",
     None,
     "Your tokenizer should not allow a pattern declaration without an identifier"],

    ["""p3
  (
    F4 L
  )4
q

P""",
     None,
     "Your tokenizer should not allow a pattern declaration without an identifier"],

    ["""p
  (
    F4 L
  )4
q

P""",
     None,
     "Your tokenizer should not allow a pattern declaration without an identifier"],

    # Edge Assertions - Incorrectly Placed Comments
    ["""p/* la la la ... */0
  (
    F2 L
  )2 (
    F2 R
  )2
q

(
  P0
)2""",
     None,
     "Your tokenizer should throw an error whenever there are comments before numbers (stray numbers)"],

    ["""p// la la la ...
0
  (
    F2 L
  )2 (
    F2 R
  )2
q

(
  P0
)2""",
     None,
     "Your tokenizer should throw an error whenever there are comments before numbers (stray numbers)"],

    ["""p0
  (
    F/* Catch us if you can ;) */2 L
  )2 (
    F2 R
  )2
q

(
  P0
)2""",
     None,
     "Your tokenizer should throw an error whenever there are comments before numbers (stray numbers)"],

    ["""p0
  (
    F2 L
  )2 (
    F2 R
  )/* Now I"m here :p */2
q

(
  P0
)2""",
     None,
     "Your tokenizer should throw an error whenever there are comments before numbers (stray numbers)"],

    ["""p0
  (
    F2 L
  )2 (
    F2 R
  )2
q

(
  P// And here! ;)
0
)2""",
     None,
     "Your tokenizer should throw an error whenever there are comments before numbers (stray numbers)"]

]

# ***************************************************************


TESTS_THE_TOKENIZER3 = [

    # Invocation of non-existing patterns
    ["""p134
  F3 L F4 R F5 R F6 L
q

P1341""",
     ["p134", "F3", "L", "F4", "R", "F5", "R", "F6", "L", "q", "P1341"],
     ""],

    ("((F2LP0F2RP3)5(P4P77P143P0)8)13",
     ["(", "(", "F2", "L", "P0", "F2", "R", "P3", ")5", "(", "P4", "P77", "P143", "P0", ")8", ")13"],
     ""),

    # Unmatched items
    ["""p37
  F47 L F55 R

P37""",
     ["p37", "F47", "L", "F55", "R", "P37"],
     ""],

    ["F F F L  F F F F F R)10()23478",
     ["F", "F", "F", "L", "F", "F", "F", "F", "F", "R", ")10", "(", ")23478"],
     ""],

    # Pattern definition within parentheses
    ["( p30 F93847 q P30 )100",
     ["(", "p30", "F93847", "q", "P30", ")100"],
     ""]

]

# ***************************************************************


TESTS_THE_COMPILER_1 = [

    # Description Example in Converter section
    ["p0FFLFFR((FFFR)2(FFFFFL)3)4qp1FRqp2FP1qp3FP2qp4FP3qP0P1P2P3P4",
     ["F", "F", "L", "F", "F", "R",
      "F", "F", "F", "R", "F", "F", "F", "R",
      "F", "F", "F", "F", "F", "L",
      "F", "F", "F", "F", "F", "L",
      "F", "F", "F", "F", "F", "L",
      "F", "F", "F", "R", "F", "F", "F", "R",
      "F", "F", "F", "F", "F", "L",
      "F", "F", "F", "F", "F", "L",
      "F", "F", "F", "F", "F", "L",
      "F", "F", "F", "R", "F", "F", "F", "R",
      "F", "F", "F", "F", "F", "L",
      "F", "F", "F", "F", "F", "L",
      "F", "F", "F", "F", "F", "L",
      "F", "F", "F", "R", "F", "F", "F", "R",
      "F", "F", "F", "F", "F", "L",
      "F", "F", "F", "F", "F", "L",
      "F", "F", "F", "F", "F", "L",
      "F", "R",
      "F", "F", "R",
      "F", "F", "F", "R",
      "F", "F", "F", "F", "R"
      ], ""],

    # Description Example in Converter section - Pattern Invocation before Definition
    ["P0P1P2P3P4p0FFLFFR((FFFR)2(FFFFFL)3)4qp1FRqp2FP1qp3FP2qp4FP3q",
     ["F", "F", "L", "F", "F", "R",
      "F", "F", "F", "R", "F", "F", "F", "R",
      "F", "F", "F", "F", "F", "L",
      "F", "F", "F", "F", "F", "L",
      "F", "F", "F", "F", "F", "L",
      "F", "F", "F", "R", "F", "F", "F", "R",
      "F", "F", "F", "F", "F", "L",
      "F", "F", "F", "F", "F", "L",
      "F", "F", "F", "F", "F", "L",
      "F", "F", "F", "R", "F", "F", "F", "R",
      "F", "F", "F", "F", "F", "L",
      "F", "F", "F", "F", "F", "L",
      "F", "F", "F", "F", "F", "L",
      "F", "F", "F", "R", "F", "F", "F", "R",
      "F", "F", "F", "F", "F", "L",
      "F", "F", "F", "F", "F", "L",
      "F", "F", "F", "F", "F", "L",
      "F", "R",
      "F", "F", "R",
      "F", "F", "F", "R",
      "F", "F", "F", "F", "R"
      ], ""],

    # A few more examples based on Description code snippets
    ["""p0
  (
    F2 L
  )2 (
    F2 R
  )2
q

(
  P0
)2""",
     ["F", "F", "L", "F", "F", "L", "F", "F", "R", "F", "F", "R", "F", "F", "L", "F", "F", "L", "F", "F", "R", "F", "F",
      "R"], ""],

    ["""// The global scope can "see" P1 and P2
p1
  // P1 can see P2, P3 and P4
  p3
    // P3 can see P1, P2 and P4 though invoking
    // P1 will likely result in infinite recursion
    F L
  q
  p4
    // Similar rules apply to P4 as they do in P3
    F P3
  q

  F P4
q
p2
  // P2 can "see" P1 and therefore can invoke P1 if it wishes
  F3 R
q

(
  P1 P2
)2 // Execute both globally defined patterns twice""",
     ["F", "F", "F", "L", "F", "F", "F", "R", "F", "F", "F", "L", "F", "F", "F", "R"], ""],

    ["""p1
  p1
    F R
  q

  F2 P1 // Refers to "inner" (locally defined) P1 so no infinite recursion results
q

(
  F2 P1 // Refers to "outer" (global) P1 since the
  // global scope can"t "see" local P1
)4

/*
  Equivalent to executing the following raw commands:
  F F F F F R F F F F F R F F F F F R F F F F F R
*/""",
     ["F", "F", "F", "F", "F", "R", "F", "F", "F", "F", "F", "R", "F", "F", "F", "F", "F", "R", "F", "F", "F", "F", "F",
      "R"], ""],

    # Edge Assertions - patterns defined but not invoked
    ["p0FFLFFR((FFFR)2(FFFFFL)3)4qp1FRqp2FP1qp3FP2qp4FP3q",
     [], ""],

    # Edge Assertions - multiple pattern ID clashes but each in different scopes
    ["""
p2017
  (
    P666 P1024
  )4
q
p1024
  p666
    p1024
      p666
        p1024
          L
        q

        F P1024
      q

      F P666
    q

    F P1024
  q

  F P666
q
p666
  p1024
    p666
      p1024
        p666
          R
        q

        F P666
      q

      F P1024
    q

    F P666
  q

  F P1024
q

P2017
""",
     ["F", "F", "F", "F", "R", "F", "F", "F", "F", "L", "F", "F", "F", "F", "R", "F", "F", "F", "F", "L", "F", "F", "F",
      "F", "R", "F", "F", "F", "F", "L", "F", "F", "F", "F", "R", "F", "F", "F", "F", "L"],
     ""],

    # Edge Assertion - A nested pattern definition should be able to see the global scope
    ["""
p0
  p2
    p0
      (
        P1
      )2
    q

    (
      P0
    )2
  q

  (
    P2
  )
q

(
  P0
)

p1
  F7 R
q
""",
     ["F", "F", "F", "F", "F", "F", "F", "R", "F", "F", "F", "F", "F", "F", "F", "R", "F", "F", "F", "F", "F", "F", "F",
      "R", "F", "F", "F", "F", "F", "F", "F", "R"],
     ""],

    ["""
p0
  p2
    p0
      (
        P1
      )2
    q

    (
      P0
    )2
  q

  (
    P2
  )
q

(
  P0
)

p1
  p0
    p2
      p1
        p0
          p2
            p1
              F R
            q

            F P1
          q

          F P2
        q

        F P0
      q

      F P1
    q

    F P2
  q

  F P0
q
""",
     ["F", "F", "F", "F", "F", "F", "F", "R", "F", "F", "F", "F", "F", "F", "F", "R", "F", "F", "F", "F", "F", "F", "F",
      "R", "F", "F", "F", "F", "F", "F", "F", "R"],
     ""],

    # Edge Assertion - Infinite recursion and invoking non-existent patterns
    # should be a runtime error
    ["""
p0
  (
    (
      (
        (
          F2 L F3 R
        )2
      )
    )2
  )2
q
p1
  F3 P1 F2
q
p2
  F L P3 F R
q
p3
  F R P2 F L
q
p4
  p1
    F3 P1 F2
  q
  p2
    F L P3 F R
  q
  p3
    F R P2 F L
  q

  L P1 R P2 L P3 R
q
p5
  F5 (
    P16
  )5 L2
q

P0
""",
     ["F", "F", "L", "F", "F", "F", "R", "F", "F", "L", "F", "F", "F", "R", "F", "F", "L", "F", "F", "F", "R", "F", "F",
      "L", "F", "F", "F", "R", "F", "F", "L", "F", "F", "F", "R", "F", "F", "L", "F", "F", "F", "R", "F", "F", "L", "F",
      "F", "F", "R", "F", "F", "L", "F", "F", "F", "R"],
     ""]
]

# ***************************************************************


TESTS_THE_COMPILER_2 = [

    # Unmatched brackets/pattern definition sequences
    ["""
p0
  (
    F2 R F4 L
  q
)5

P0
""",
     None,
     "An error should be thrown at the converter if brackets and/or pattern definition tokens are unmatched"],

    # Placing pattern definitions within a bracketed sequence
    ["""
(
  P0

  p0
    F2 R F4 L
  q
)13
""",
     None,
     "An error should be thrown at the converter if one or more pattern definitions are nested by a bracketed sequence"],

    ["""
p1
  (
    P0

    p0
      F2 R F4 L
    q
  )13
q
""",
     None,
     "Nesting pattern definitions in bracketed sequences should be a compile-time error not a runtime error"],

    # Infinite recursion
    ["""
p1
  R P1 L
q

P1
""",
     None,
     "An infinitely recursive sequence should throw an error if invoked"],

    ["""
p3
  F11 P2
q
p2
  P3 F5
q

P2
""",
     None,
     "An infinitely recursive sequence should throw an error if invoked"],

    ["""
P10

p10
  p3
    F11 P2
  q
  p2
    P3 F5
  q

  P2
q
""",
     None,
     "An infinitely recursive sequence should throw an error if invoked"],

    # Invoking a non-existent pattern
    ["P1337",
     None,
     "voking a non-existent pattern (in the global scope) should throw an error"],

    ["""
p3017
  F5 (
    P1337
  )3 R2
q

P3017
""",
     None,
     "Invoking a non-existent pattern (in the global scope) should throw an error"],

    # Invoking a pattern invisible to the current scope
    ["""
p1
  p2
    F5 L F4 R
  q
q
p3
  (
    P2
  )2
q

P3
""",
     None,
     "Invoking a pattern not visible to the current scope should yield identical behavior as invoking a non-existent pattern"],

    ["""
p1
  p2
    // empty!
  q
q
p3
  (
    P2
  )2
q

P3 // should still throw an error
""",
     None,
     "Invoking a pattern not visible to the current scope should yield identical behavior as invoking a non-existent pattern"]

]

# ***************************************************************


TESTS_THE_MACHINE_1 = [

    ["""/*
  RoboScript Ultimatum (RSU)
  A simple and comprehensive code example
*/

// Define a new pattern with identifier n = 0
p0
  // The commands below causes the MyRobot to move
  // in a short snake-like path upwards if executed
  (
    F2 L // Go forwards two steps and then turn left
  )2 (
    F2 R // Go forwards two steps and then turn right
  )2
q

// Execute the snake-like pattern twice to generate
// a longer snake-like pattern
(
  P0
)2""",
     "*  \r\n*  \r\n***\r\n  *\r\n***\r\n*  \r\n***\r\n  *\r\n***",
     ""]
]

# ***************************************************************


TESTS_EXECUTE_1 = [

    ["""\
/*
  RoboScript Ultimatum (RSU)
  A simple and comprehensive code example
*/

// Define a new pattern with identifier n = 0
p0
  // The commands below causes the MyRobot to move
  // in a short snake-like path upwards if executed
  (
    F2 L // Go forwards two steps and then turn left
  )2 (
    F2 R // Go forwards two steps and then turn right
  )2
q

// Execute the snake-like pattern twice to generate
// a longer snake-like pattern
(
  P0
)2""",
     """\
*  \r
*  \r
***\r
  *\r
***\r
*  \r
***\r
  *\r
***\
""",
     ""]

]
