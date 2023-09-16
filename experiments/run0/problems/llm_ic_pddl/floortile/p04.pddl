(define (problem p01-543)
 (:domain floor-tile)
 (:objects tile_0-1 tile_0-2 tile_0-3 tile_0-4
           tile_1-1 tile_1-2 tile_1-3 tile_1-4
           tile_2-1 tile_2-2 tile_2-3 tile_2-4
           tile_3-1 tile_3-2 tile_3-3 tile_3-4
           tile_4-1 tile_4-2 tile_4-3 tile_4-4 - tile
           robot1 robot2 - robot
           white black - color
)
 (:init 
   (= (total-cost) 0)
   (robot-at robot1 tile_0-3)
   (robot-at robot2 tile_3-4)
   (robot-has robot1 white)
   (robot-has robot2 black)
   (available-color white)
   (available-color black)
   (clear tile_0-1)
   (clear tile_0-2)
   (clear tile_0-4)
   (clear tile_1-1)
   (clear tile_1-2)
   (clear tile_1-3)
   (clear tile_1-4)
   (clear tile_2-1)
   (clear tile_2-2)
   (clear tile_2-3)
   (clear tile_2-4)
   (clear tile_3-1)
   (clear tile_3-2)
   (clear tile_3-3)
   (clear tile_4-1)
   (clear tile_4-2)
   (clear tile_4-3)
   (clear tile_4-4)
   ;; Add the rest of the up, down, left, right relations here
)
 (:goal (and
    (painted tile_1-1 white)
    (painted tile_1-2 black)
    (painted tile_1-3 white)
    (painted tile_1-4 black)
    (painted tile_2-1 black)
    (painted tile_2-2 white)
    (painted tile_2-3 black)
    (painted tile_2-4 white)
    (painted tile_3-1 white)
    (painted tile_3-2 black)
    (painted tile_3-3 white)
    (painted tile_3-4 black)
    (painted tile_4-1 black)
    (painted tile_4-2 white)
    (painted tile_4-3 black)
    (painted tile_4-4 white)
))
 (:metric minimize (total-cost))
)