package Homework.Java.Homework.Task3;

import java.util.ArrayList;
import java.util.List;

public class Tasks2 {
    public static void main(String[] args) {
        Integer[] arr = new Integer[]{1, 2, 3, 4, 5, 6, 7, 8, 9};
        removeEvenNumbers(arr);
    }

    public static void removeEvenNumbers(Integer[] arr) {
        List <Integer> numbers = new ArrayList<Integer>();
        for (Integer el : arr) {
            numbers.add(el);
        }
        numbers.removeIf(n -> (n % 2 == 0));
        System.out.println(String.valueOf(numbers));

    }
}







// import java.util.Arrays;
// import java.util.ArrayList;

// class Answer {
//     public static void removeEvenNumbers(Integer[] arr) {
//         ArrayList<Integer> ints = new ArrayList<>(Arrays.asList(arr));
//         for (int i = 0; i < ints.size(); i++) {
//             if (ints.get(i) % 2 == 0) {
//                 ints.remove(i);
//                 i--;
//             }
//         }
//         System.out.println(ints);
//     }
// }

// public class Printer{ 
//     public static void main(String[] args) { 
//       Integer[] arr = {};

//       if (args.length == 0) {
//         arr = new Integer[]{1, 2, 3, 4, 5, 6, 7, 8, 9};
//       }
//       else{
//         arr = Arrays.stream(args[0].split(", "))
//                         .map(Integer::parseInt)
//                         .toArray(Integer[]::new);
//       }     

//       Answer ans = new Answer();      
//       ans.removeEvenNumbers(arr);
//     }
// }