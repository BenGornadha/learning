object Flattener {
    fun flatten2(source: Collection<Any?>): List<Any> =  source.map { potentialNestedList ->
            if (potentialNestedList is Collection<*>) flatten2(potentialNestedList) else listOf(potentialNestedList)
        }.flatten().filterNotNull()

    fun flatten(source: Collection<Any?>): List<Any> =  source.flatMap { potentialNestedList ->
        if (potentialNestedList is Collection<*>) flatten(potentialNestedList) else listOf(potentialNestedList)
    }.filterNotNull()

}


