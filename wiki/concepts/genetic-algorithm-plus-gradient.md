---
type: concept
aliases: ["GA + SQP", "two-stage optimizer"]
tags: [optimization, mdo]
source_count: 1
---

# Genetic algorithm + gradient

## Definition

Two-stage optimizer used in David's MDO thesis: a genetic algorithm picks discrete variables (material choice, structural topology), then sequential quadratic programming (SQP) refines the continuous variables to a local minimum within the GA's selection. Combines exploration with local convergence.

## Appears in

- [[videos/multidisciplinary-design-optimization-2016-masters-thesis-presentation]]

## Related

- [[concepts/multidisciplinary-optimization]]
- [[concepts/pareto-front]]
- [[entities/projects/cubesat-mdo-thesis-2016]]
