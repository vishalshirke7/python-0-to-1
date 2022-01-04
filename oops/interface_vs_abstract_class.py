"""
CONSIDER USING ABSTRACT CLASSES IF :

When we talk about abstract classes we are defining characteristics of an object type; specifying what an object is.

You want to share code among several closely related classes.
You expect that classes that extend your abstract class have many common methods or fields, or require access modifiers other than public (such as protected and private).
You want to declare non-static or non-final fields.

abstract class: To implement the same or different behaviour among multiple related objects. It establishes "IS A" relation.
An abstract class can have shared state or functionality
A good abstract class will reduce the amount of code that has to be rewritten because it's functionality or state can be shared.


CONSIDER USING INTERFACES IF :

You expect that unrelated classes would implement your interface. For example,many unrelated objects can implement Serializable interface.
You want to specify the behaviour of a particular data type, but not concerned about who implements its behaviour.
You want to take advantage of multiple inheritance of type.

interface: To implement a contract by multiple unrelated objects. It provides "HAS A" capability.
An interface is only a promise to provide the state or functionality. 
The interface has no defined information to be shared

When we talk about an interface and define capabilities that we promise to provide, 
we are talking about establishing a contract about what the object can do.

This was ery helpful: Interfaces do not express something like "a Doberman is a type of dog and every dog can walk"
 but more like "this thing can walk".

Example:

Abstract class ( IS A relation)

Reader is an abstract class.

BufferedReader is a Reader

FileReader is a Reader

FileReader and BufferedReader are used for common purpose : Reading data, and they are related through Reader class.

Interface ( HAS A capability )

Serializable is an interface.

Assume that you have two classes in your application, which are implementing Serializable interface

Employee implements Serializable

Game implements Serializable

Here you can't establish any relation through Serializable interface between Employee and Game, which are meant for different purpose. 
Both are capable of Serializing the state and the comparasion ends there.

"""