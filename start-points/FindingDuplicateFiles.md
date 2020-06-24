Finding Duplicate Files
=======================

When doing backups of media files such as images, movies and music, a common problem is knowing which files are already backed-up and which are not. The simple solution to this is to over-backup, just backup "everything" always. That is an OK solution if you got infinte amount of backup space. It's not so great a solution if you've got limited space, since you end up with the same old christmas pictures scattered at five different places on your oh-so-untidy backup drive, and even more importantly, it is not so interesting to see the same picture for the 5th time when you sit down to watch through the gallery with your dear ones!

One solution to this massive-duplication-of-files problem is finding the duplicates, and deleting them. Of course, I *really* want to trust software that finds duplicate files among the pictures and movies that are irreplaceable.

This kata is about making sure you trust such an algorithm implementation by writing high quality tests.

Things to think about:

 * What does it mean for a file to be identical to another file? Name? File size? Content? Date-of-creation?
 * How do you specify the input to the algorithm? Should you use some kind of mock of the file system, or something else?
 * What is the output of the algorithm? A list of paths, or something else?

To answer those questions, try to come up with concrete examples, instead of "drawing a castle in the sky".

To get you started, here are a few examples:
 * The source folder contains a single file "A.txt" which is empty. The result should be that no files are duplicated.
 * The source folder contains two files, "A.txt" and "B.txt", both are empty. The output should specify that A and B are identical.
 * The source folder contains three files "A", "B" and "C" in different subdirectories. The content is "123", "456" and "123" respectively. The output should explain that "A" and "C" are identical.
