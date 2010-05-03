(defun write-file (filename contents)
  (with-open-file (out filename
                   :direction :output
                   :if-exists :supersede)
    (with-standard-io-syntax
      (format out contents))))

(write-file (format NIL "src/ObjectA.uc") "class ObjectA extends Object;")
(write-file (format NIL "src/ObjectB.uc") "class ObjectB extends Object;")
