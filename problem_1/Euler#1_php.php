
<?php
/* Euler Problem #1

        If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
        The sum of these multiples is 23.

        Find the sum of all the multiples of 3 or 5 below 1000.*/
        
  
function mult_of_num ($range, $num)

      
 /* (int, int) -> list of ints

           return a list of all the multiples of num given the range of range

           */ 
{
    $i=1; 
    $list=array(); 
    
       while ($i < $range)
              {

                  if ($i%$num == 0)
                  {
                      array_push($list, $i);
                      $i = $i + 1;
                  };

                  $i = $i + 1;
              }

        return($list); 
}

function remove_dupe_lists($list, $num1, $num2)

/* (array, int, int) -> array

          return an array with any indexed value that is both divisible by num1 and num2 removed. removes duplicates from the two lists for the multiples.

           */
{
    $i=1;  
    print_r($list);
    while ($i <= sizeof($list))
    {
        if ( $list[$i-1]%$num1==0 && $list[$i-1]%$num2==0)

                    {
                      array_splice($list,($i-1),1);
                    }

                    $i = $i +1;
    }
    return $list;
}

function add_lists($list1, $list2)

 /* (list, list) -> int

         return the sum of all the indexed values in array1 and array2

          */
{
    $result = 0; 
    
    foreach($list1 as $num)
    {
         
        $result = $result + $num; 
    }
    foreach($list2 as $num)
    {
        
        $result = $result + $num; 
    }
    echo $result; 
    return $result; 
}

$five_list = mult_of_num(1000,5);
$three_list = mult_of_num(1000, 3); 

add_lists(remove_dupe_lists($five_list,3,5), $three_list);




?>