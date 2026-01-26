Explanation: 
- When taking position2 and position1, the offset of these positions 
is the translation that would need to be made in order to move the 
1 in position1 to the position where the 1 exists in img2 (position2)

- If the offset produced by this translation occurs multiple times, 
then we can think of the overlap of this translation as the 
frequency of offsets that exist for this particular translation

- ==**Think of it this way:**== 
    -   if we applied a particular translation (offset) to img1,
    then every time a 1 from img1 lands on a position in img2
    that also contains a 1, we accrue a unit of overlap
    -   therefore, the number of times a given offset occurs
        corresponds to how many 1s overlap under that translation 
