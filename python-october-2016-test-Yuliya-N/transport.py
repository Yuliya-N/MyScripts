"""
Implement class(es) structure to describe transport network like following:
(You can open `transport.html` in browser for pretty schema)

*******************************************************
*             .-----air 90m 120$-----.                *
*  +-----+   /                        \   +-----+     *
*  |Milan|<-+-------train 3h 70$-------+->|Paris|     *
*  +-----+                                +-----+     *
*     ^ ^                                  ^  ^       *
*     | |                                  |  |       *
*     | |                                  | train    *
*     | +                                  |  1h      *
*     |  \               .---air 40m 100$-'  150$     *
*     |  air 1h         |                     |       *
*    air  120$          |                     |       *
*    2h     \          .-.                +---+-----+ *
*    200$    '------->|FRA|<----train---->|Frankfurt| *
*     |                '-'  10m 20$       +---------+ *
*     |                 ^                     ^       *
*   .-+-.               |                     |       *
*  | KBP |<---air 2h---'                      |       *
*   '---'      200$                           |       *
*     ^                                     train     *
*     |                                    45m 40$    *
*  bus 1h 5$                                  |       *
*     |                                       |       *
*     v                                       v       *
*  +--+---+                               +------+    *
*  | Kyiv |                               |Berlin|    *
*  +------+                               +------+    *
*******************************************************

There should be
1. Classes for places (Cities, Airports, Bus stations etc)
2. Classes for connections/routes
    - Every connection links 2 places.
    - Connections may be single- or double-linking –
       you can go KBP->Milan, but not Milan->KBP
    - Every connection have time and price
3. Any other classes/functions you find usefull for this
4. Based on your classes/functions, there should be possibility to implement
    to find fastest/cheapest route. You may not introduce this,
    only ensure possibility for this

"""
