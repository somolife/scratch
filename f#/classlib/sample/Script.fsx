#load "sample.fs"
open sample

// Define your library scripting code here

let add x y = x + y

let square x = x * x

let squareAdd x y = add x y |> square

let isVowel (c: char) =
    match c with
    | 'a' | 'e' | 'i' |'o' |'u'
    | 'A' | 'E' | 'I' | 'O' | 'U' -> true
    |_ -> false

let toPigLatin (word: string) =    
    if isVowel word.[0] then
        word + "yay"
    else
        word.[1..] + string(word.[0]) + "ay"

let rec quicksort list =
   match list with
   | [] ->                            // If the list is empty
        []                            // return an empty list
   | firstElem::otherElements ->      // If the list is not empty  
        let smallerElements =         // extract the smaller ones  
            otherElements             
            |> List.filter (fun e -> e < firstElem) 
            |> quicksort              // and sort them
        let largerElements =          // extract the large ones
            otherElements 
            |> List.filter (fun e -> e >= firstElem)
            |> quicksort              // and sort them
        // Combine the 3 parts into a new list and return it
        List.concat [smallerElements; [firstElem]; largerElements]
// test
// printfn "%A" (quicksort [1;5;23;18;9;1;3]) ;;

let rec quicksort2 = function
   | [] -> []                         
   | first::rest -> 
        let smaller,larger = List.partition ((>=) first) rest 
        List.concat [quicksort2 smaller; [first]; quicksort2 larger]
        
// test
// printfn "%A" (quicksort2 [1;5;23;18;9;1;3]) ;;

// [1;2;3] |> List.map (fun x -> x + 1) |> printfn "%A" ;;


let rec fib = function // this does not use tail recursion so it's pretty inefficient
   | n when n = 0 -> 0
   | n when n = 1 -> 1
   | n -> fib(n-1) + fib(n-2)

