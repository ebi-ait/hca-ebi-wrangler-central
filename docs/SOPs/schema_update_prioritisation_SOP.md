---
layout: default
title: Schema update prioritisation SOP
parent: SOPs
---
<script src="https://kit.fontawesome.com/fc66878563.js" crossorigin="anonymous"></script>

# # Prioritising schema updates SOP
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Purpose of this SOP

This document describes the process of prioritising schema updates. It focuses on the early stages of schema updates:
Discovery and prioritisation of next updates
Responsibilities
This document will not cover the steps required to make an actual schema change. Those steps are covered in the following documents:
- [DCP2 specs - Changing the metadata schema](https://github.com/HumanCellAtlas/dcp2/blob/main/docs/dcp2_system_design.rst#1changing-the-hca-metadata-schema): This document describes the procedure to follow when creating a PR to change the schema
- [Metadata Schema repository - commiters](https://github.com/HumanCellAtlas/metadata-schema/blob/master/docs/committers.md) : This document describes how to create a schema update PR.
- [Metadata Schema repository - release process](https://github.com/HumanCellAtlas/metadata-schema/blob/master/docs/release_process.md): pre-release and release process for schema updates.

## Flow summary chart
<div class="mxgraph" style="max-width:100%;border:1px solid transparent;" data-mxgraph="{&quot;highlight&quot;:&quot;#000000&quot;,&quot;nav&quot;:true,&quot;resize&quot;:true,&quot;toolbar&quot;:&quot;zoom layers lightbox&quot;,&quot;edit&quot;:&quot;_blank&quot;,&quot;xml&quot;:&quot;&lt;mxfile host=\&quot;app.diagrams.net\&quot; modified=\&quot;2021-09-14T12:18:00.968Z\&quot; agent=\&quot;5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36\&quot; etag=\&quot;rOVFe34DR4c1xDoU3gFB\&quot; version=\&quot;15.0.6\&quot; type=\&quot;google\&quot;&gt;&lt;diagram id=\&quot;K5tSO0vCFDweOvvXe_7b\&quot; name=\&quot;Page-1\&quot;&gt;5VrbcqM4EP0aV+0+2MUd/GjnNjWVTVLx7I7zlBIggxKMKCHGdr5+JCPu2JDYTnaSp6DWBdF91Oe0nIF6tlxfERD5/2AXBgNFctcD9XygKMpYM9gfbtmkFllStdTiEeQKW2GYoReYDRTWBLkwrgykGAcURVWjg8MQOrRiA4TgVXXYAgfVt0bAgw3DzAFB0/oTudRPrZZiFvZvEHl+9mbZGKc9S5ANFl8S+8DFq5JJvRioZwRjmj4t12cw4N7L/JLOu9zRm2+MwJC2TPg3huTWfuI+UaQA2Cww20HptACFz2nbp5S7csInKpfQRkOA6MhD1E/sEcLM5jtgyO0rAkIvgGTosDcSwDZzObu9i9mf2PHhEjwmkQsofIwIwgRRFAOKcPjIxox8umTD1YhgB8ZxuoXsQ7S5G+LF9eTl++LHBE+H1Le+D+XCQ/mXx3STRYXgJHQhX0AeqNOVjyicRcDhvWyXEbNt35h2x5Tg5zx6KrMsUBCc4QCT7WrqYgENx8lHlnpcc2xLEutpOlv4/xckFK5LJrHnK4iXkJINGyJ6VV0gPzsKGcRXBa7ksTgvfglT+VkAAstevnYRbvYgHJU1SwA4ABACCA5essa3ZAlC/pIJDQAPPNsGYDEHwxQBzILiOIG8S1bHcrH0D0A8KL7n0Q4Ae1k3CIxPh4EsF+yDgCGdDAKNJNJ+9sRXgSARrs6iK22jK9JZEQmW2SL+6GInWW6d0xUOO43dtZ0ZatFwAbQWrdEwHAvai+NEQ6tFQ2mJhtISDe31wejneeWret78aM+rX9TzyodjXvuqnv9wzMtmw7fQZeJXNDGhPvZwCIKLwjotWJdTYjHmGuNIePcJUroRSh4kFFeDAdeIzkvPD3ypkS5a52ux8raxyRpMb27m5cZDuVFM2rb4LEXPmneQIOYvSMSYphLYGdsYJ8SBXQKFFSQlcdM6Tjiae3cvUggMmGb+VS092uIupt5hFNICYbl6zCAm69Ul0g8Ss2roybfRBqhd2vGnKAl4AQao4w+TaKAYAT+TNjMaHn9aQkhR6LExf/EqAsLnYPP3ftXJznY88jBmawvpmZ929sjV5fxmqsX/xdOre+lydoPv5UjDZqxbxsbcPAQXsXwDL6fJ01xhQWdljYvogWLU3CtGs6TECscAJz1yUlSCpZhUQmq3XoWyq0OzLWeNDVMFxpH0qlwj6nHPpGWdtGSZVRmCo0YK4ZqP4i9N69B4P8TeWth0AsXqBZQD2KsTG+/DZ6pZw4ZlNLHRVswcBxv9OG7cUBdNzgvdCb8o4geRBT9GTjthSWXCKtMVPwAlwlIyLutmnh28NtL3MNveSrSTscyejJWd+07KKgVbb4l1ZjuQ2dRxFWu6WcPQDmZrLqTXVFidIlPPvIEie2quZnF9uwqZnlIke5MmsnMYIy9kCYwbC4KtoZbydNdyxZEd9hCHsJYZhAkEbHkOdgaeLdfwI48YB01ExxK57lbrtSWmqv47RhoxamlEbaEYqwVaysl0cbMYvLvnn1m+vWy9iJKOcBH1PsRu1CvwtpuoNmI3Xu/1XSx+m1DGvl08fdobaVzZw35YaHuJ/TOgII/uCVDw9utIoweHl+pWGNh4VS5ZtwbWkeW5LZ325Py8MH0o9by9SDWqXG7lzVNWqbLWk/T7lqkfxPl10PXlfK2Gcr1+mb6D8xlCwKY0LOID4t0b1qzqe1St8oMce0hXPK6gsI50OnyWIV9wSHudj3eQst0SVf1fwVWvK8u6PukLV0PacTl+ZLjqpl7dsPQOcM2c8gXhqn1SuNaVZP2++o+Ga7Nca8L1APAVeOu60M7kxmtVyQGyQf0zkW3W8mfjt/O+yDZrR0SuC5A33xWwZvF/P+nw4t+n1Ivf&lt;/diagram&gt;&lt;/mxfile&gt;&quot;}"></div>
<script type="text/javascript" src="https://viewer.diagrams.net/js/viewer-static.min.js"></script>

## Process

### Ticket acknowledgement

Every 2 weeks, the **designated wrangler** will review and update the [rolling ticket](​​https://github.com/HumanCellAtlas/metadata-schema/issues/1391) with the new issues that are not already collected. 

### Wrangler catch-up

On the bi-weekly wrangler catch-ups, one of the points will be to discuss and prioritise the next set of schema updates. In order for new priorities to be set, the next requirements must be fulfilled:
1. Both schema updates had an outcome (Accepted/rejected) and made it to production (In the accepted scenario)
1. The desired schema updates must be gathered in a ticket that will hold information about what changes are needed and why.
1. The tickets need to be listed in the [rolling ticket](​​https://github.com/HumanCellAtlas/metadata-schema/issues/1391)

If condition 1 is met, the former **designated wrangler** will proceed to close the [priority ticket](#creating-a-priority-ticket) from the previous iteration. The wranglers will then discuss what are the next priorities, based on what is needed to ingest new datasets, get a more accurate representation of the metadata, or based on community/system requirements. 

Once a decision is reached based on majority, the wranglers will then assign a new designated wrangler for that 2 week period, who will overlook the process from here on and assign responsibilities on PR creation.

Condition 1 is necessary and refers to workflow, whereas conditions 2 and 3 are needed for tracking but not essential to continue with the process. If condition 1 fails, the designated wrangler for that priority ticket will report on the reasons why and, if more time is deemed necessary, this item in the agenda will be skipped until the next meeting.

### Creating a priority ticket

The designated wrangler, based on the conversation during the catch-up meeting, will create a ticket in the following 3 working days, using the [template provided](https://github.com/ebi-ait/hca-ebi-wrangler-central/issues/new?assignees=&labels=operations,next&template=schema_priority_ticket.md&title=Schema+update+priority+ticket+-+YYYY-MM-DD). This ticket will be used to track the next set of priorities, and will contain the following information:
- List of changes that will be prioritised next (max 2)
- Each ticket assigned to the wrangler that will create the PR. The wrangler may be the same for both tickets, and in some cases it may be the same as the designated wrangler.

This ticket will be then presented to the wider DCP community, on the dcp-2 slack channel, for them to review and ask questions about prioritisation. The message should contain an established deadline for review (2 working days), after which if no objection is made, the designated wrangler will start working on the schema changes. Please take a look at the [message template](#template-messages) provided in this SOP

If there are objections, they will need to be discussed and there should be an action to perform. If that action is detrimental (time-wise) to one schema update but doesn't affect the other, the designated wrangler should take the decision to go ahead with the unaffected schema update or wait until the other issue is resolved.

### Outcomes

After both PRs are accepted or rejected, the **designated wrangler** will be in charge of commenting on the outcome in the ticket, effectively closing it on the catch-up meeting or extending the deadline for another 2 weeks if there are discussions or unplanned inconveniences.

### PR process

The PR process is covered on the other documents listed in the “objectives” section of the document.

## Template messages

### DCP-2 slack channel message
> Hi team! Just so everybody knows, we are going to work on the following set of schema updates:
> <Schema_update_1>
> <Schema_update_2>
>
> They are all reflected in this ticket <link to ticket>. If you want to give your input, please do so before the end of <2 working days from the day the message is sent>. This ticket represents the next set of schema changes the wranglers would like to prioritise.
