[Week 2] Architect: Planning
============================

Summary
-------

Today we went over the basics of planning. Specifically, we covered top-down
and bottom-up programming.  They each have their pros and cons:

- Top-down programming is great for when you have a big idea but you aren't sure where to start.  It's useful
to break things into smaller pieces.
- Bottom-up programming is good for building incremental code. Each additional piece you add
is built on top of what you have.  This allows for you to build incremental tests, have
minimum working examples at all times, and not get lost in a code base that is too complicated.

Each should be used in different situations.  However, when completing a project,
both situations come up.  For the Architect project, they can both be used in the following
ways:

1. Use top-down programming to decompose your idea into smaller and smaller chunks
2. As you decompose, identify the chunks that lie just above the actual code
3. With these chunks identified, begin the bottom-up programming in which you write
incremental code.  This means you increase the complexity and size of your code
one feature at a time.

During class, you were all assigned to teams.  Each team spent time planning
a project.  You were supposed to decompose the goal into specific parts and then
plan out the minimum working examples.

Expected Homework
-----------------

- You should progress on the minimum working examples.
- The code base you build should be incremental.
- Every feature you add should be wrapped into a function when appropriate.

  - For example, if you have 1 function that builds an entire Ferris Wheel, then this is incorrect.
  - You should have functions that build the parts and then a function that puts them together.
  - Further, each part function could use functions that do common things, such as make circles or triangles.

- By next week, you should have made progress on the project.
- You should make it through two milestones.

Resources
---------

Coming soon: resources for structuring your project across multiple files.


Slides
------


.. raw:: html

    <iframe src="https://docs.google.com/presentation/d/1rEue0K_9SUw2VF0FV3935XLBK2FUaVJEJ3Y-gIvaZOY/embed?start=false&loop=false&delayms=30000" frameborder="0" width="480" height="299" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
