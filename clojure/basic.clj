(str "hello world!")

(+ 1 2 3)
; => 6

(if true
  "By Zeus's hammer!"
  "By Aquaman's trident!")
  ; => "By Zeus's hammer!"

(if false
  "By Zeus's hammer!"
  "By Aquaman's trident!")
  ; => "By Aquaman's trident!"


(if true
  (do (println "Success!")
      "By Zeus's hammer!")
  (do (println "Failure!")
      "By Aquaman's trident!"))

(* 1/3 6)

(hash-map :a 1 :b 2)
(get {:a 0 :b 1} :b)
(get [3 2 1] 0)

