<!-- fg=black bg=cyan -->

# Trustless Bridges

### By: Hernando Castano | @hernando:matrix.parity.io

```
                                           ^^
      ^^      ..                                       ..
              []                                       []
            .:[]:_          ^^                       ,:[]:.
          .: :[]: :-.                             ,-: :[]: :.
        .: : :[]: : :`._                       ,.': : :[]: : :.
      .: : : :[]: : : : :-._               _,-: : : : :[]: : : :.
  _..: : : : :[]: : : : : : :-._________.-: : : : : : :[]: : : : :-._
  _:_:_:_:_:_:[]:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:[]:_:_:_:_:_:_
  !!!!!!!!!!!![]!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!![]!!!!!!!!!!!!!
  ^^^^^^^^^^^^[]^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^[]^^^^^^^^^^^^^
              []                                       []
              []                                       []
              []                                       []
   ~~^-~^_~^~/  \~^-~^~_~^-~_^~-^~_^~~-^~_~^~-~_~-^~_^/  \~^-~_~^-~~-
  ~ _~~- ~^-^~-^~~- ^~_^-^~~_ -~^_ -~_-~~^- _~~_~-^_ ~^-^~~-_^-~ ~^
     ~ ^- _~~_-  ~~ _ ~  ^~  - ~~^ _ -  ^~-  ~ _  ~~^  - ~_   - ~^_~
       ~-  ^_  ~^ -  ^~ _ - ~^~ _   _~^~-  _ ~~^ - _ ~ - _ ~~^ -
  jgs     ~^ -_ ~^^ -_ ~ _ - _ ~^~-  _~ -_   ~- _ ~^ _ -  ~ ^-
              ~^~ - _ ^ - ~~~ _ - _ ~-^ ~ __- ~_ - ~  ~^_-
                  ~ ~- ^~ -  ~^ -  ~ ^~ - ~~  ^~ - ~
```

---
<!-- fg=black bg=cyan-->

## Presentation Outline

- What is a Bridge?
- Types of Bridges
- Rialto Bridge
- Future Plans

---
<!-- effect=stars -->

## Demo Prep - RLT

---
<!-- fg=black bg=green -->

## What is a Bridge?

tl;dr: A way to connect two unrelated chains

### Types of Bridges
- Custodial
- Collateral
- Trustless

---
<!-- fg=black bg=green -->

## Custodial Bridges

[Chain A] -> [Central Party] -> [Chain B]

- You send your Chain A token to the central party
- Expectation is that they will credit your Chain B account correctly

[BTC] -> [wBTC Foundation] -> [ETH]

- Example: Wrapped BTC on Ethereum

---
<!-- fg=black bg=green -->

## Collateral Backed Bridges (XClaim)

+----------------------+            +----------------------+
|  BTC                 |            |                 ETH  |
|           +-------+  |            |   +-------+          |
|     1     |       |  |     0      |   |       |          |
|   +---->  | Vault | +-------------->  |  S.C  | +--+     |
|   |       |       |  |            |   |       |    |     |
|   |       +-------+  |            |   +-------+    | 3   |
|   |                  |            |                |     |
|   |                  |            |       ^        v     |
|   +                  |     2      |       |              |
| Alice  +----------------------------------+      Alice   |
|                      |            |                      |
+----------------------+            +----------------------+

---
<!-- fg=black bg=green -->

## Trustless Bridges

[Chain A] -> [Chain B]

- Basically an on-chain light client for a foreign chain
- Light clients only follow headers and keep no state

[Chain A Headers] -> [Chain B]

- A light client will track headers of the source chain
- If applicable, needs to keep track of finality

---
<!-- fg=black bg=blue-->

# Rialto Bridge

---
<!-- fg=black bg=blue-->

## Rialto Bridge

[PoA Ethereum] <-> [Substrate]

- Two way trustless bridge between an Ethereum PoA chain and a Substrate chain
- Ethereum chain is using Aura consensus
- Substrate chain is using Grandpa consensus
- Repo: https://github.com/paritytech/parity-bridges-common

---
<!-- fg=black bg=blue-->

## Authority Round (Aura) Consensus

- Designed in Parity Ethereum days for stable a test network
- Blocks are produced at regular intervals by trusted authorities
- Authorities implicitly vote on blocks by building on blocks
- A block is considered finalized if it has (n/2) + 1 votes
- If we had three validators: (3/2) + 1 = 2

[A] <- [B] <- [C]
 |      |
 |      --- Finalized when C is built
 --- Finalized when B is built

---
<!-- fg=black bg=blue-->

## Grandpa Consensus

- Authorities are staked
- Authorities vote on chains of blocks which they think are final
- Authority sets change periodically
- Blocks that signal these changes have a special log in the header

```
          / [C1] <- [D1]
[A] <- [B] <- [C2] <- [D2]
                  \ [D3] <- [E3]
```

---
<!-- fg=black bg=blue-->

## Rialto Architecture

   OpenEthereum Node                    Substrate Node

+-------------------+                +-------------------+
|                   |                |                   |
| Substrate Header  |                |  Ethereum Bridge  |
| Light Client      |                |  Pallet           |
|                   |                |                   |
|                   |                |  Currency Exchange|
| Grandpa Finality  |                |  Pallet           |
| Precompile        |                |                   |
|                   |                |                   |
|                   |                |                   |
|                   |                |                   |
+-------------------+                +-------------------+

---
<!-- fg=black bg=blue -->

## Bridge Relay

 +--------+       +--------+
 |       |       |       |
 |  ETH  |       |  SUB  |
 |       |       |       |
 +--+----+       +-----+-+
    ^                  ^
    |                  |
    |    +--------+    |
RPC |    |        |    |  RPC
    |    | Relay  |    |
    +--> |        | <--+
         +--------+

---
<!-- fg=black bg=blue-->

## Rialto Applications

+----------------------------------------|
|                                        |
|          Currency Exchange             |
|                                        |
+----------------------------------------+
|                                        |
|         Light Client Base Layer        |
|                                        |
+----------------------------------------+

---
<!-- fg=black bg=blue-->

## Rialto Applications

+----------------------------------------+
|                                        |
|          Your Application!             |
|                                        |
+----------------------------------------+
|                                        |
|          Message Dispatch              |
|                                        |
+----------------------------------------+
|                                        |
|          Message Delivery              |
|                                        |
+----------------------------------------+
|                                        |
|         Light Client Base Layer        |
|                                        |
+----------------------------------------+

---
<!-- fg=black bg=blue -->

## Eth2Sub Header Sync

```
Rialto PoA             Bridge Relay             Substrate

     +                      +                      +
     |                      |  Best ETH header?    |
     |                      | +------------------> |
     |                      |                      |
     |                      |    I know about X    |
     | Any newer header?    | <------------------+ |
     | <------------------+ |                      |
     |                      |                      |
     |                      |                      |
     |  Yep, here you go    |                      |
     | +------------------> |                      |
     |                      | New headers incoming |
     |                      | +------------------> |
     |                      |                      |
     |                      |                      | +----+
     |                      |                      |      | Verify headers
     |                      |                      | <----+
     |                      |                      |
     |                      |                      | +----+
     |                      |                      |      | Import headers
     |                      |                      | <----+
     |                      |                      |
     +                      +                      +
```
---
<!-- fg=black bg=blue -->

## Eth2Sub Currency Exchange

```
      Rialto PoA             Bridge Relay             Substrate

Lock RLT   +                      +                      +
   +-----+ |                      |                      |
   |       |                      |                      |
   +-----> |                      |                      |
           |    Any CE Txs?       |                      |
           | <------------------+ |                      |
           |                      |                      |
           |   Yep, here ya go    |                      |
           | +------------------> |                      |
           |                      |  Tx Inclusion Proof  |
           |                      | +------------------> | +-----+
           |                      |                      |       | In finalized header?
           |                      |                      | <-----+
           |                      |                      | +-----+
           |                      |                      |       | Credit Funds
           |                      |                      | <-----+
           +                      +                      +
```

---
<!-- fg=black bg=magenta -->

# Future Plans
---
<!-- fg=black bg=magenta -->

## Future Plans

[DOT] <-> [KSM]

- Want to connect Substrate based chains
- Important for sovereign chain communication
- Potentially implement a bridge parachain

[DOT::Call] <-> [KSM::Call]

- Arbitrary message passing between Substrate chains

[ETH] <-> [DOT]

- Want to connect Ethereum mainnet to Substrate chains
- More of a support role to other teams (e.g Snowfork)

[DOT] <-> [DOGE]

- Who wouldn't want to see this?

---
<!-- effect=fireworks-->

# Shout-Outs
Slava Nikolsky (@svyatonik)
Tomek Drwięga (@tomusdrw)
Thibaut Sardan (@tbaut)
