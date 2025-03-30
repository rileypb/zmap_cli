
/*
 Original copyright Terence Parr; see below. Modifications for zmap made by Philip Riley.
*/

/*
 [The "BSD licence"]
 Copyright (c) 2013 Terence Parr
 All rights reserved.

 Redistribution and use in source and binary forms, with or without
 modification, are permitted provided that the following conditions
 are met:
 1. Redistributions of source code must retain the above copyright
    notice, this list of conditions and the following disclaimer.
 2. Redistributions in binary form must reproduce the above copyright
    notice, this list of conditions and the following disclaimer in the
    documentation and/or other materials provided with the distribution.
 3. The name of the author may not be used to endorse or promote products
    derived from this software without specific prior written permission.

 THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
 IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
 OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
 IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT,
 INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
 NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
 DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
 THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
 THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
*/
/** Derived from http://www.graphviz.org/doc/info/lang.html.
    Comments pulled from spec.
 */
grammar zmap;

parse
   : graph+
   ;

graph
   : id_ '{' stmt_list '}'
   ;

stmt_list
   : ( stmt ';'? )*
   ;

stmt
   : node_stmt | edge_stmt | attr_stmt  
   ;

attr_stmt
   : ( GRAPH | NODE | EDGE ) attr_list
   ;

attr_list
   : ( '[' a_list? ']' )+
   ;

a_list
   : ( attr ','? )* attr
   ;

attr
   : id_ ( '=' id_ )? 
   | id_ '=' tuple_ 
   ;

tuple_
   : '(' id_ ',' id_ ')'
   ;

edge_stmt
   : ( node_id_left ) edgeRHS attr_list?
   ;

edgeRHS
   : edgeop ( node_id_right | unknown | dark_unknown )
   ;

unknown
   : '?'
   ;

dark_unknown
   : '!'
   ;

edgeop
   : '-->' | '<->'
   ;

node_stmt
   : node_id attr_list?
   ;

node_id
   : id_ special?
   ;

node_id_left
   : id_ port_left
   ;

node_id_right
   : port_right? id_ special? 
   ;

special
   : '*'
   ;

port_left
   : ':' id_
   ;

port_right
   : id_ ':'
   ;

id_
   : ID | STRING | NUMBER
   ;

// "The keywords node, edge, and graph are case-independent"


GRAPH
   : 'map'
   ;

NODE
   : 'room'
   ;


EDGE
   : 'passage'
   ;



/** "a numeral [-]?(.[0-9]+ | [0-9]+(.[0-9]*)? )" */ NUMBER
   : '-'? ( '.' DIGIT+ | DIGIT+ ( '.' DIGIT* )? )
   ;


fragment DIGIT
   : [0-9]
   ;


/** "any double-quoted string ("...") possibly containing escaped quotes" */ STRING
   : '"' ( '\\"' | . )*? '"'
   ;


/** "Any string of alphabetic ([a-zA-Z\200-\377]) characters, underscores
 *  ('_') or digits ([0-9]), not beginning with a digit"
 */ ID
   : LETTER ( LETTER | DIGIT )*
   ;


fragment LETTER
   : [a-zA-Z\u0080-\u00FF_]
   ;


COMMENT
   : '/*' .*? '*/' -> skip
   ;


LINE_COMMENT
   : '//' .*? '\r'? '\n' -> skip
   ;



WS
   : [ \t\n\r]+ -> skip
   ;